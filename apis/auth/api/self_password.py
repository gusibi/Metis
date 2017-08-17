# -*- coding: utf-8 -*-

from sanic.response import text

from . import Resource
from .. import schemas


class SelfPassword(Resource):

    async def post(self, request):
        print(request.json)
        return {'hahahha': 1234}, 201
        return {}, 201, None

    async def put(self, request):
        print(request.json)
        print(request.headers)
        return {'hahahha': 1234}

        return {}, 200, None