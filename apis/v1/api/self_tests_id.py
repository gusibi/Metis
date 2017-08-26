# -*- coding: utf-8 -*-

from bson.objectid import ObjectId

from apis.models.test import Test
from apis.verification import current_account
from apis.exception import NotFound, BadRequest

from . import Resource
from .. import schemas


class SelfTestsId(Resource):

    async def get(self, request, id):
        test = Test.get(_id=id)
        if not test or test.get('creator_id') != current_account.id:
            raise NotFound('test_not_found')
        return test, 200

    async def put(self, request, id):
        test = Test.get(_id=id)
        if not test or test.get('creator_id') != current_account.id:
            raise NotFound('test_not_found')
        result = Test.find_one_and_update(filter={'_id': ObjectId(id)},
                                          update={'$set': request.json})
        return result, 200

    async def delete(self, request, id):
        test = Test.get(_id=id)
        if not test or test.get('creator_id') != current_account.id:
            raise NotFound('test_not_found')
        if test.status == 'published':
            raise BadRequest('invalid_status')
        Test.delete_one(_id=id)
        return {}, 204