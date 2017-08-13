# -*- coding: utf-8 -*-

from sanic.response import text

from . import Resource
from .. import schemas


class SelfTests(Resource):

    async def get(self, request):
        print(request.headers)
        print(request.args)

        return [], 200, None

    async def post(self, request):
        print(request.json)
        print(request.headers)

        return {'id': 'something', 'title': 'something', 'description': 'something'}, 201, None