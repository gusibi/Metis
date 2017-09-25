# -*- coding: utf-8 -*-

from sanic.response import text, json

from apis.models.oauth import Account
from apis.exception import BadRequest
from apis.verification import get_wxapp_userinfo

from . import Resource



class AccountsWxapp(Resource):

    async def post(self, request):
        encrypted_data = request.json.get('username')
        iv = request.json.get('password')
        code = request.json.get('code')
        user_info = get_wxapp_userinfo(encrypted_data, iv, code)
        openid = user_info.get('openId')
        account = Account.get_by_wxapp(openid=openid)
        if account:
            raise BadRequest('wxapp_already_registered')
        params = {
            'nickname': user_info['nickName'],
            'avatar': user_info['avatarUrl'],
            'authentications': {'wxapp': openid},
        }
        account.update(**params)
        account.save()
        return account, 201
