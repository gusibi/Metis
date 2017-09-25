# -*- coding: utf-8 -*-

from bson.objectid import ObjectId

from apis.models.test import Test, Question
from apis.verification import current_account
from apis.exception import NotFound

from . import Resource


class SelfTestsTestIdQuestionsId(Resource):

    async def post(self, request, test_id, id):
        test = Test.objects(id=test_id).first()
        if not test or test.creator_id != current_account.id:
            raise NotFound('test_not_found')
        question = Question.objects(id=id, test_id=test_id).first()
        if not question:
            raise NotFound('question_not_found')
        question.udpate(**request.json)
        question.save()
        return question, 200
