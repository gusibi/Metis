# -*- coding: utf-8 -*-

from time import time
from sanic.response import text

from qcloud_cos.cos_auth import Auth

from apis.settings import Config

from . import Resource


class QcCosConfig(Resource):

    async def get(self, request):
        auth = Auth(appid=Config.QCOS_APPID,
                    secret_id=Config.QCOS_SECRET_ID,
                    secret_key=Config.QCOS_SECRET_KEY)
        expired = time() + 3600
        dir_name = request.raw_args.get('cos_path', '/xrzeti')
        sign = auth.sign_more(Config.QCOS_BUCKET_NAME,
                              cos_path=dir_name,
                              expired=expired)
        return {"sign": sign}, 200