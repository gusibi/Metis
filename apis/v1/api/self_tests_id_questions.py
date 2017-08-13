# -*- coding: utf-8 -*-

from sanic.response import text

from . import Resource
from .. import schemas


class SelfTestsIdQuestions(Resource):

    async def get(self, request, id):
        print(request.headers)

        return {'title': 'something', 'options': []}, 200, None

    async def post(self, request, id):
        print(request.json)
        print(request.headers)

        return {'title': 'something', 'options': []}, 201, None