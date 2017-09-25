# -*- coding: utf-8 -*-

from bson.objectid import ObjectId

from apis.models.test import Test
from apis.verification import current_account
from apis.exception import NotFound, BadRequest
from apis.helpers import format_result, split_datetime, str_to_time

from . import Resource


class SelfTestsId(Resource):

    def _get_test(self, id):
        test = Test.objects(id=id).first()
        if not test or test.creator_id != current_account.id:
            raise NotFound('test_not_found')
        return test

    async def get(self, request, id):
        test = self._get_test(id)
        return test, 200

    async def put(self, request, id):
        test = self._get_test(id)
        start_time = request.json.get('start_time')
        if start_time:
            request.json['start_time'] = str_to_time(start_time)
        end_time = request.json.get('end_time')
        if end_time:
            request.json['end_time'] = str_to_time(end_time)
        test.update(**request.json)
        test.save()
        return test, 200

    async def delete(self, request, id):
        test = self._get_test(id)
        if test.status == 'published':
            raise BadRequest('invalid_status')
        test.delete()
        return {}, 204
