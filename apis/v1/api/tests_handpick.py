# -*- coding: utf-8 -*-

from sanic.response import text
from apis.models.test import Test

from . import Resource



class TestsHandpick(Resource):

    async def get(self, request):
        filter = {'status': 'published'}
        tests = Test.objects(**filter).order_by('-created_time')
        print(tests)
        for test in tests:
            print(test.id, test.title, test.creator)
        return tests, 200