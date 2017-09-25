# -*- coding: utf-8 -*-

from sanic.response import text

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
        questions = Question.objects(test_id=test.id).all()
        return questions, 200

    async def post(self, request, id):
        test = self._get_test(id)
        request.json['test_id'] = test.id
        request.json['id'] = generation_objectid()
        question = Question(**request.json).save()
        return question, 201
