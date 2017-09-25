# -*- coding: utf-8 -*-

from datetime import datetime

from apis.models.test import Test, Question, Answer
from apis.exception import NotFound
from apis.verification import current_account


from . import Resource


class TestsIdAnswers(Resource):

    async def post(self, request, id):
        test = Test.objects(id=id).first()
        if not test or test.status != 'published':
            raise NotFound('test_not_found')
        question_id = request.json['question_id']
        options = request.json['options']
        question = Question.objects(test_id=id, id=question_id).first()
        if not question:
            raise NotFound('question_not_found')
        answer = Answer.objects(account_id=current_account.id,
                                test_id=test.id).first()
        if not answer:
            Answer(account_id=current_account.id,
                   test_id=test.id,
                   answers={question_id: options},
                   updated_time=datetime.utcnow()).save()
        else:
            answers = answer.answers
            answers[question_id] = options
            answer.update(answers=answers, updated_time=datetime.utcnow())
            answer.save()

        return {'ok': True}, 201