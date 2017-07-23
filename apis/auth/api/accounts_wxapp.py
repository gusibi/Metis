# -*- coding: utf-8 -*-

from sanic.response import text, json

from apis.models.oauth import Account

from . import Resource
from .. import schemas


class AccountsWxapp(Resource):

    async def post(self, request):
        username = request.json.get('username')
        account = Account.get(username=username)
        if account:
            return json({'error_code': 'username_already',
                         'message': 'Username already exists'},
                         status=400
                        )
        account = Account.insert(username=username,
                                 password=request.json['password'])
        return account, 200