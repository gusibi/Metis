# -*- coding: utf-8 -*-


from apis.models.test import Test, Question
from apis.exception import NotFound

from . import Resource


class TestsIdQuestions(Resource):

    def _get_test(self, id):
        test = Test.objects(id=id).first()
        if not test:
            raise NotFound('account_not_found')
        return test

    async def get(self, request, id):
        test = self._get_test(id)
        questions = Question.objects(test_id=test.id).order_by('number').all()
        return questions, 200
