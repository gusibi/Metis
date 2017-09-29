# -*- coding: utf-8 -*-

from apis.models.test import Test, Answer
from apis.exception import NotFound

from . import Resource


class TestsIdScore(Resource):

    def _get_test(self, id):
        test = Test.objects(id=id).first()
        if not test or test.status == 'draft':
            raise NotFound('account_not_found')
        return test

    async def get(self, request, id):
        answer = Answer.objects(test_id=id).first()
        if not answer:
            raise NotFound('answer_not_found')
        return answer, 200
