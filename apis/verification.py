# -*- coding: utf-8 -*-

import base64
import time
import jwt

from apis.models.oauth import Account


def get_authorization(request):
    authorization = request.headers.get('Authorization')
    if not authorization:
        return False, None
    try:
        authorization_type, token = authorization.split(' ')
        return authorization_type, token
    except ValueError:
        return False, None


def verify_client(client_id, secret):
    pass


def verify_request(request):
    authorization_type, token = get_authorization(request)
    if authorization_type == 'Basic':
        is_validate = verify_basic_token(token)
        if not is_validate:
            return False, None
    elif authorization_type == 'Bearer':
        return verify_bearer_token(token)
    return False, None


def verify_password(username, password):
    account = Account.get(username=username, password=password)
    if account:
        return account
    else:
        return {}


def verify_wxapp(openid, password):
    pass


def verify_code(code):
    pass


def create_token(request):
    grant_type = request.json.get('grant_type')
    username = request.json['username']
    password = request.json['password']
    if grant_type == 'password':
        account = verify_password(username, password)
    elif grant_type == 'wxapp':
        account = verify_wxapp(username, password)
    if not account:
        return {}
    payload = {
        "iss": "gusibi.com",
         "iat": int(time.time()),
         "exp": int(time.time()) + 86400 * 7,
         "aud": "www.gusibi.com",
         "sub": str(account['_id']),
         "username": account['username'],
         "scopes": ['open']
    }
    print(payload)
    token = jwt.encode(payload, 'secret', algorithm='HS256')
    return True, {'access_token': token, 'account_id': str(account['_id'])}

def verify_basic_token(token):
    try:
         client = base64.b64decode(token)
         client_id, secret = client.split(':')
    except (TypeError, ValueError):
         return False, None
    return verify_client(client_id, secret)


def verify_bearer_token(token):
    payload = jwt.decode(token, 'secret', audience='www.gusibi.com', algorithms=['HS256'])
    if payload:
        return True, token
    return False, token
