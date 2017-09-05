# -*- coding: utf-8 -*-

from bson.objectid import ObjectId

from apis.models.test import Test, Question
from apis.verification import current_account
from apis.exception import NotFound

from . import Resource


class SelfTestsTestIdQuestionsId(Resource):

    async def post(self, request, test_id, id):
        test = Test.get(_id=test_id)
        if not test or test.get('creator_id') != current_account.id:
            raise NotFound('test_not_found')
        question = Question.get(_id=id)
        if not question or question.get('test_id') != test_id:
            raise NotFound('question_not_found')
        result = Question.find_one_and_update(filter={'_id': ObjectId(id)},
                                              update={'$set': request.json})
        return result, 200, None
