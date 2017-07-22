from os import environ
from six.moves.urllib.parse import urlparse


class Config(object):

    DEBUG = False
    TESTING = False

    SECRET_KEY = 'MDzEfbh7e63UjRCDepoKN8NiFNBssezyL'

    MONGO_MASTER_HOST = environ.get('MONGO_PORT_27017_TCP_ADDR', '127.0.0.1')
    MONGO_MASTER_PORT = environ.get('MONGO_PORT_27017_TCP_PORT', '27017')
    MONGO_DATABASE = environ.get('MONGO_DATABASE', 'metis')
    MONGO_MASTER_URL = 'mongodb://%s:%s' % (MONGO_MASTER_HOST,
                                            MONGO_MASTER_PORT)

    APP_TRANSPORT = environ.get('APP_TRANSPORT', 'http')
    APP_DOMAIN = environ.get('APP_DOMAIN', 'http://metis.gusibi.mobi')
    API_DOMAIN = environ.get('API_DOMAIN', 'http://metis.gusibi.mobi')
    DOMAIN = '%s://%s' % (APP_TRANSPORT, urlparse(APP_DOMAIN).netloc)

    # 微信 小程序账号信息
    WXAPP_ID = environ.get('WXAPP_ID', 'appid')
    WXAPP_SECRET = environ.get('WXAPP_SECRET', '')
    WXAPP_TOKEN = environ.get('WXAPP_TOKEN', 'token')
    WXAPP_ENCODINGAESKEY = environ.get('WXAPP_ENCODINGAESKEY', '')

    # cdn 使用 腾讯云
