# -*- coding: utf-8 -*-

from sanic.response import text

from . import Resource
from .. import schemas


class AccountsSelf(Resource):

    async def get(self, request):
        print(request.headers)

        return {'id': 'something'}, 201, None