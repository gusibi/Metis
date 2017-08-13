# -*- coding: utf-8 -*-

from sanic.response import text

from . import Resource
from .. import schemas


class TestsId(Resource):

    async def get(self, request, id):
        print(request.headers)

        return {'id': 'something', 'title': 'something', 'description': 'something'}, 200, None