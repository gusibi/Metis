# -*- coding: utf-8 -*-

from sanic.response import text

from . import Resource
from .. import schemas


class SelfTestsTestIdQuestionsId(Resource):

    async def post(self, request, test_id, id):
        print(request.json)
        print(request.headers)

        return {'title': 'something', 'options': []}, 200, None