# -*- coding: utf-8 -*-

from sanic.response import text

from apis.verification import current_account
from apis.exception import NotFound
from apis.models.oauth import Account
from . import Resource


class AccountsSelf(Resource):

    async def get(self, request):
        if not current_account.id:
            raise NotFound('account_not_found')
        account = Account.get(current_account.id)
        if not account:
            raise NotFound('account_not_found')
        return account, 200
