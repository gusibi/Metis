# -*- coding: utf-8 -*-

from bson.objectid import ObjectId

from apis.models.test import Test
from apis.verification import current_account
from apis.exception import NotFound, BadRequest
from apis.helpers import format_result, split_datetime, str_to_time

from . import Resource


class SelfTestsId(Resource):

    @format_result(fields=['created_time', 'start_time', 'end_time'])
    async def get(self, request, id):
        test = Test.get(_id=id)
        if not test or test.get('creator_id') != current_account.id:
            raise NotFound('test_not_found')
        _start_time = test.get('start_time')
        if _start_time:
            test['date_start'], test['time_start'] = split_datetime(_start_time)
        _end_time = test.get('end_time')
        if _end_time:
            test['date_end'], test['time_end'] = split_datetime(_end_time)
        return test, 200

    async def put(self, request, id):
        test = Test.get(_id=id)
        if not test or test.get('creator_id') != current_account.id:
            raise NotFound('test_not_found')
        start_time = request.json.get('start_time')
        if start_time:
            request.json['start_time'] = str_to_time(start_time)
        end_time = request.json.get('end_time')
        if end_time:
            request.json['end_time'] = str_to_time(end_time)
        result = Test.find_one_and_update(filter={'_id': ObjectId(id)},
                                          update={'$set': request.json})
        return result, 200

    async def delete(self, request, id):
        test = Test.get(_id=id)
        if not test or test.get('creator_id') != current_account.id:
            raise NotFound('test_not_found')
        if test.get('status') == 'published':
            raise BadRequest('invalid_status')
        Test.delete_one(_id=id)
        return {}, 204
