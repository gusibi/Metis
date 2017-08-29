# -*- coding: utf-8 -*-

from sanic.response import text
from apis.models.test import Test

from . import Resource



class TestsHandpick(Resource):

    async def get(self, request):
        filter = {'status': 'published'}
        tests = Test.find(filter=filter, sorts=[('created_time', 1)])
        return tests, 200