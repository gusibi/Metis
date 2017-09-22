#! -*- coding: utf-8 -*-
import bcrypt
from hashlib import sha256
from binascii import hexlify
from datetime import datetime

from pymongo import TEXT
from pymongo.operations import IndexModel
from pymodm import MongoModel, EmbeddedMongoModel, fields


__all__ = ['Account', 'OAuth2Client']


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


class Account(MongoModel):

    '''
    帐号
    :param _id: account ID
    :param username: 用户ID
    :param created_time: 创建时间
    :param password: 密码
    :param authentications: 认证信息 {'wxapp': 'openid', 'mobile': 'mobile_num'}
    :param status: 状态(active|发布|forbidden)
    '''

    collection_name = 'account'

    id = fields.ObjectIdField(primary_key=True, required=True)
    username = fields.CharField(required=True)
    password = fields.CharField(required=True)
    authentications = fields.DictField()
    created_time = fields.DateTimeField(default=datetime.utcnow())
    updated_time = fields.DateTimeField()

    class Meta:
        # Text index on content can be used for text search.
        indexes = [IndexModel([('username', TEXT)])]

    @classmethod
    def get_by_wxapp(cls, openid):
        account = cls.get(**{'authentications.wxapp': openid})
        return account


class OAuth2Client(MongoModel):

    collection_name = 'oauth2_client'

    client_id = fields.CharField(primary_key=True, required=True)
    account_id = fields.ObjectIdField(required=True)
    secret = fields.CharField(required=True)
    scopes = fields.ListField(required=True)
    created_time = fields.DateTimeField(default=datetime.utcnow())