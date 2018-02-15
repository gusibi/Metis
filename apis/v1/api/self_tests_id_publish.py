# -*- coding: utf-8 -*-

from apis.models.test import Test
from apis.verification import current_account
from apis.exception import NotFound, BadRequest

from . import Resource


class SelfTestsIdPublish(Resource):

    def _get_test(self, id):
        test = Test.objects(id=id).first()
        if not test or test.creator_id != current_account.id:
            raise NotFound('test_not_found')
        return test

    async def put(self, request, id):
        test = self._get_test(id)
        if not test.question_count:
            raise BadRequest('no_questions')
        test.update(status=Test.STATUS_PUBLISHED)
        return test, 200

    async def delete(self, request, id):
        test = self._get_test(id)
        if test.status == Test.STATUS_PUBLISHED:
            test.update(status=Test.STATUS_WITHDRAW)
        return {}, 204
