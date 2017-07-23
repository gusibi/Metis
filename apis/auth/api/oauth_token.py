# -*- coding: utf-8 -*-

from sanic.response import text

from apis.verification import verify_request
from apis.models.oauth import Account

from . import Resource
from .. import schemas


class OauthToken(Resource):

    async def post(self, request):
        token = verify_request(request)
        print(token)
        return token
