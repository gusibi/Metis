# -*- coding: utf-8 -*-

from sanic.response import text

from apis.models.test import Test, Question
from apis.verification import current_account
from apis.exception import NotFound

from . import Resource
from .. import schemas


class SelfTestsIdQuestions(Resource):

    async def get(self, request, id):
        print(request.headers)
        test = Test.get(_id=id)
        if not test or test.get('creator_id') != current_account.id:
            raise NotFound('account_not_found')
        questions = Question.find(filter={'test_id': id}, skip=0, limit=20)
        return questions, 200

    async def post(self, request, id):
        test = Test.get(_id=id)
        if not test or test.get('creator_id') != current_account.id:
            raise NotFound('account_not_found')
        request.json['test_id'] = id
        question = Question.insert(**request.json)
        return question, 201, None