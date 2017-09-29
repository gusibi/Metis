# -*- coding: utf-8 -*-

from apis.models.test import Test, Question
from apis.verification import current_account
from apis.exception import NotFound

from apis.models import generation_objectid

from . import Resource


class SelfTestsIdQuestions(Resource):

    def _get_test(self, id):
        test = Test.objects(id=id).first()
        if not test or test.creator_id != current_account.id:
            raise NotFound('account_not_found')
        return test

    async def get(self, request, id):
        test = self._get_test(id)
        questions = Question.objects(test_id=test.id).order_by('number').all()
        return questions, 200

    async def post(self, request, id):
        test = self._get_test(id)
        question_count = Question.objects(test_id=id).count()
        request.json['test_id'] = test.id
        request.json['number'] = question_count
        request.json['id'] = generation_objectid()
        question = Question(**request.json).save()
        # update test questions count
        test.update(question_count=question_count + 1)
        test.save()
        return question, 201
