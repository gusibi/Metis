# -*- coding: utf-8 -*-

from sanic.response import text

from apis.verification import create_token
from apis.models.oauth import Account

from . import Resource
from .. import schemas


class OauthToken(Resource):

    async def post(self, request):
        is_validate, token = create_token(request)
        print(token)
        return token
