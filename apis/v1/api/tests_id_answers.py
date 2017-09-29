# -*- coding: utf-8 -*-

from datetime import datetime

from apis.models import generation_objectid
from apis.models.test import Test, Question, Answer
from apis.exception import NotFound
from apis.verification import current_account


from . import Resource


class TestsIdAnswers(Resource):

    def calculate_score(self, test, answers):
        questions = Question.objects(test_id=test.id).order_by('number').all()
        correct_answers = {}
        for question in questions:
            for option in question.options:
                if option.get('is_checked'):
                    correct_answers.setdefault(question.id, []).append(option['index'])
        corrent_count = 0
        for qid, answer in answers.items():
            if correct_answers.get(qid) == answer:
                corrent_count += 1
        score = test.total_score / test.question_count * corrent_count
        return score

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
            Answer(
                id=generation_objectid(),
                account_id=current_account.id,
                test_id=test.id,
                answers={question_id: options},
                updated_time=datetime.utcnow()).save()
        else:
            answers = answer.answers
            answers[question_id] = options
            answer.update(answers=answers, updated_time=datetime.utcnow())
            answer.save()
        if question.number == test.question_count - 1:
            last = True
            score = self.calculate_score(test, answer.answers)
            answer.update(score=score, status='finished')
            # 统计分数
        else:
            last = False
        return {'ok': True, 'last': last}, 201
