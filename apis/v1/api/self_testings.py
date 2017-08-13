# -*- coding: utf-8 -*-

from sanic.response import text

from . import Resource
from .. import schemas


class SelfTestings(Resource):

    async def get(self, request):
        print(request.headers)
        print(request.args)

        return [], 200, None