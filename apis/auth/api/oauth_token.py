# -*- coding: utf-8 -*-

from sanic.response import text

from . import Resource
from .. import schemas


class OauthToken(Resource):

    async def post(self, request):
        print(request.json)
        print(request.headers)

        return {'account_id': 'something', 'access_token': 'something', 'refresh_token': 'something', 'token_type': 'Bearer', 'expires_in': 9573, 'scopes': 'something'}, 201, None