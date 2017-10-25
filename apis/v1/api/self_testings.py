# -*- coding: utf-8 -*-

from apis.helpers import get_offset_limit
from apis.models.test import Answer, Test
from apis.verification import current_account

from . import Resource


class SelfTestings(Resource):

    async def get(self, request):
        filter = {'account_id': current_account.id}
        status = request.args.get('status')
        if status:
            filter['status'] = status
        offset, limit = get_offset_limit(request.raw_args)
        answers = (Answer.objects(**filter)
                   .order_by('-update_time')
                   .skip(offset).limit(limit))
        test_ids = [a.test_id for a in answers]
        tests = Test.objects(id__in=test_ids).all()
        return tests, 200
