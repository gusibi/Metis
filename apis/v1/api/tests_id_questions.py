# -*- coding: utf-8 -*-

from sanic.response import text

from . import Resource
from .. import schemas


class TestsIdQuestions(Resource):

    async def get(self, request, id):
        print(request.headers)

        return [], 200, None