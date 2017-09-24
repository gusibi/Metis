# -*- coding: utf-8 -*-

from sanic.response import text

from apis.models.test import Test
from apis.exception import NotFound

from . import Resource


class TestsIdQuestions(Resource):

    async def get(self, request, id):
        test = Test.objects(id=id).first()
        if not test or test.status != 'published':
            raise NotFound('test_not_found')
        return test.questions, 200