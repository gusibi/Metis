# -*- coding: utf-8 -*-

from sanic.response import text

from apis.verification import create_token
from apis.models.oauth import Account
from apis.exception import Unauthorized

from . import Resource
from .. import schemas


class OauthToken(Resource):

    async def post(self, request):
        is_validate, token = create_token(request)
        if not is_validate:
            raise Unauthorized('unauthorized', 'Invalid token', '用户未注册')
        return token, 201
