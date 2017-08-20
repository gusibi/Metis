# -*- coding: utf-8 -*-

from sanic.response import text

from apis.models.test import Test
from apis.exception import NotFound

from . import Resource


class TestsId(Resource):

    async def get(self, request, id):
        print(request.headers)
        test = Test.get(_id=id)
        if not test or test.get('status') != 'published':
            raise NotFound('test_not_found')

        return test, 200
