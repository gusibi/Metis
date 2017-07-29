#! -*- coding: utf-8 -*-
import bcrypt
from hashlib import sha256
from binascii import hexlify
from datetime import datetime

from apis.models import Model


__all__ = ['Account', 'OAuth2Client', 'OAuth2Token']


class HasedPassword(object):

    HASH_LOG_ROUNDS = 4  # 值越大 hash 速度越慢，越安全，4 最小值

    def __init__(self, hashed):
        super(HasedPassword, self).init()
        self.hashed = hashed

    def __eq__(self, plain):
        return self.check(plain)

    def __ne__(self, plain):
        return not self.check(plain)

    def check(self, plain):
        plain = HasedPassword.digest(plain)
        return bcrypt.hashpw(plain, self.hashed) == self.hashed

    @classmethod
    def digest(cls, text):
        if not isinstance(text, bytes):
            text = text.encode('utf-8', 'strict')
        return hexlify(sha256(text).digest())

    @classmethod
    def hash(cls, plain):
        plain = cls.digest(plain)
        return bcrypt.hashpw(plain, bcrypt.gensalt(cls.HASH_LOG_ROUNDS))


class Account(Model):

    '''
    帐号
    :param _id: account ID
    :param username: 用户ID
    :param created_time: 创建时间
    :param password: 密码
    :param authentications: 认证信息 {'wxapp': 'openid', 'mobile': 'mobile_num'}
    :param status: 状态(active|发布|forbidden)
    '''

    __collection__ = 'account'
    __default_fields__ = {
        'created_time': datetime.utcnow()
    }

    @classmethod
    def get_by_wxapp(cls, openid):
        account = cls.get({'authentications.openid': openid})


class OAuth2Token(Model):

    __collection__ = 'oauth_token'
    __default_fields__ = {
        'created_time': datetime.utcnow()
    }


class OAuth2Client(Model):

    __collection__ = 'oauth2_client'
    __default_fields__ = {
        'created_time': datetime.utcnow()
    }
