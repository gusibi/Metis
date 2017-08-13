# -*- coding: utf-8 -*-

from sanic.response import text

from . import Resource
from .. import schemas


class SelfTestsId(Resource):

    async def put(self, request, id):
        print(request.json)
        print(request.headers)

        return {'id': 'something', 'title': 'something', 'description': 'something'}, 200, None