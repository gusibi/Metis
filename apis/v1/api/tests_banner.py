# -*- coding: utf-8 -*-

from apis.models.test import Test

from . import Resource


class TestsBanner(Resource):

    async def get(self, request):
        tests = (Test.objects(status=Test.STATUS_PUBLISHED, is_sticky=True)
                 .order_by('-participate_number')
                 .skip(0).limit(10))
        return tests, 200, None
