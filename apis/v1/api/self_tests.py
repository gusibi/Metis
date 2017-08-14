# -*- coding: utf-8 -*-

from apis.models.test import Test
from apis.helpers import get_offset_limit, str_to_time
from apis.verification import current_account

from . import Resource


class SelfTests(Resource):

    async def get(self, request):
        print(request.headers)
        print(request.raw_args)
        filter = {'creator_id': current_account.id}
        status = request.args.get('status')
        if status:
            filter['status'] = status
        offset, limit = get_offset_limit(request.raw_args)
        print(filter, offset, limit)
        tests = Test.find(filter=filter, skip=offset, limit=limit)
        print(tests)
        for test in tests:
            print(test)
        return tests, 200

    async def post(self, request):
        request.json['creator_id'] = current_account.id
        start_time = request.json.get('start_time')
        if start_time:
            request.json['start_time'] = str_to_time(start_time)
        end_time = request.json.get('end_time')
        if end_time:
            request.json['end_time'] = str_to_time(end_time)
        test = Test.insert(**request.json)
        return test, 201