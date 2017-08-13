# -*- coding: utf-8 -*-

from sanic.response import text

from . import Resource
from .. import schemas


class OauthTokenCode(Resource):

    async def post(self, request):
        print(request.json)
        print(request.headers)

        return {'account_id': 'something', 'access_token': 'something', 'token_type': 'jwt'}, 200, None