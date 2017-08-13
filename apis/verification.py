# -*- coding: utf-8 -*-

import base64
import time
import jwt
from weixin.helper import smart_str

from apis.models.oauth import Account, OAuth2Client
from apis.settings import Config
from apis.exception import Unauthorized
from apis.models import ObjectModel


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
    client = OAuth2Client.get(client_id=smart_str(client_id),
                              secret=smart_str(secret))
    if client:
        return True, client.get('scopes', [])
    return False, []


def verify_request(request):
    authorization_type, token = get_authorization(request)
    if authorization_type == 'Basic':
        return verify_basic_token(token)
    elif authorization_type == 'JWT':
        return verify_jwt_token(token)
    return False, None


def verify_password(username, password):
    account = Account.get(username=username, password=password)
    if account:
        return account
    else:
        return {}


def get_wxapp_userinfo(encrypted_data, iv, code):
    from weixin.lib.wxcrypt import WXBizDataCrypt
    from weixin import WXAPPAPI
    from weixin.oauth2 import OAuth2AuthExchangeError
    appid = Config.WXAPP_ID
    secret = Config.WXAPP_SECRET
    api = WXAPPAPI(appid=appid, app_secret=secret)
    try:
        session_info = api.exchange_code_for_session_key(code=code)
    except OAuth2AuthExchangeError as e:
        raise Unauthorized(e.code, e.description)
    session_key = session_info.get('session_key')
    crypt = WXBizDataCrypt(appid, session_key)
    user_info = crypt.decrypt(encrypted_data, iv)
    return user_info


def verify_wxapp(encrypted_data, iv, code):
    user_info = get_wxapp_userinfo(encrypted_data, iv, code)
    openid = user_info.get('openId', None)
    if openid:
        auth = Account.get_by_wxapp(openid)
        if not auth:
            raise Unauthorized('wxapp_not_registered')
        return auth
    raise Unauthorized('invalid_wxapp_code')


def create_token(request):
    # verify basic token
    approach = request.json.get('auth_approach')
    username = request.json['username']
    password = request.json['password']
    if approach == 'password':
        account = verify_password(username, password)
    elif approach == 'wxapp':
        account = verify_wxapp(username, password, request.args.get('code'))
    if not account:
        return False, {}
    payload = {
        "iss": Config.ISS,
        "iat": int(time.time()),
        "exp": int(time.time()) + 86400 * 7,
        "aud": Config.AUDIENCE,
        "sub": str(account['_id']),
        "nickname": account['nickname'],
        "scopes": ['open']
    }
    token = jwt.encode(payload, 'secret', algorithm='HS256')
    return True, {'access_token': token, 'account_id': str(account['_id'])}


def verify_basic_token(token):
    try:
         client = base64.b64decode(token)
         client_id, secret = smart_str(client).split(':')
    except (TypeError, ValueError) as e:
        return False, None
    return verify_client(client_id, secret)


def verify_jwt_token(token):
    payload = jwt.decode(token, 'secret',
                         audience=Config.AUDIENCE,
                         algorithms=['HS256'])
    if payload:
        return True, ObjectModel.object_from_dictionary(payload)
    return False, token
