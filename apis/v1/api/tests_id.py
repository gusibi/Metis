# -*- coding: utf-8 -*-

from apis.models.test import Test
from apis.exception import NotFound

from . import Resource


class TestsId(Resource):

    async def get(self, request, id):
        test = Test.objects(id=id).first()
        if not test or test.status != Test.STATUS_PUBLISHED:
            raise NotFound('test_not_found')
        return test, 200
