#! -*- coding: utf-8 -*-

from datetime import datetime

from weixin.helper import smart_str

from mongoengine import EmbeddedDocument, Document
from mongoengine.fields import (StringField, DateTimeField,
                                ObjectIdField, DictField, IntField,
                                ListField, ReferenceField,
                                BooleanField)

from apis.helpers import split_datetime
from apis.models.oauth import Account


class Question(Document):

    '''
    题目：
    :param _id: 问题 ID
    :param title: 题目
    :param test_id:  所属测试 ID
    :param number: 第几题
    :param type: 题目类型 'single_choice|multiple_choice'
    :param options: 选项
                [
                {'value': '这是第一个选项', 'index': 0, 'is_checked': True},
                {'value': '这是第二个选项', 'index': 1, 'is_checked': False},
                ]
    '''

    def __getattribute__(self, name):
        if name == 'id':
            id = super(Question, self).__getattribute__(name)
            return smart_str(id)
        return super(Question, self).__getattribute__(name)

    meta = {
        "collection_name": 'question',
        'indexes': [
            'title',
            '$title',  # text index
            ('test_id', 'number'),
        ]
    }

    id = ObjectIdField(primary_key=True, required=True)
    test_id = StringField(required=True)
    title = StringField(required=True)
    type = StringField(required=True, default='single_choice')
    number = IntField(required=True, default=0)
    options = ListField(required=True, default=[])
    created_time = DateTimeField(default=datetime.utcnow())
    updated_time = DateTimeField()


class Test(Document):

    '''
    测试
    :param _id: 测试ID
    :param creator_id: 用户ID
    :param title: 测试 title
    :param description: 测试描述
    :param remark: 备注
    :param start_time: 开始时间
    :param end_time: 结束时间
    :param order_score: 排序值
    :param status: 状态(草稿|发布|下线)
    :param is_sticky: 置顶(首页 banner)
    :param is_digest: 精华(首页精选)
    :param created_time: 创建时间
    '''

    STATUS_DRAFT = 'draft'
    STATUS_PUBLISHED = 'published'
    STATUS_WITHDRAW = 'withdraw'

    def __getattribute__(self, name):
        if name == 'id':
            id = super(Test, self).__getattribute__(name)
            return smart_str(id)
        return super(Test, self).__getattribute__(name)

    id = ObjectIdField(primary_key=True, required=True)
    creator_id = StringField(required=True)
    title = StringField(required=True)
    description = StringField(required=True)
    image = StringField()
    remark = StringField()
    status = StringField(required=True, default='draft')
    total_score = IntField(default=100)
    question_count = IntField(required=True, default=0)
    participate_number = IntField(required=True, default=0)
    start_time = DateTimeField()
    end_time = DateTimeField()
    is_sticky = BooleanField()
    is_digest = BooleanField()
    order_score = IntField()
    created_time = DateTimeField(default=datetime.utcnow())
    updated_time = DateTimeField()
    # questions = ReferenceField('Question')

    meta = {
        "collection_name": 'test',
        'indexes': [
            'title',
            '$title',  # text index
            ('creator_id', 'status', '-created_time'),
            ('is_sticky', 'status', '-order_score'),
            ('is_digest', 'status', '-order_score'),
            ('status', '-participate_number')
        ]
    }

    @property
    def creator(self):
        account = Account.objects(id=self.creator_id).first()
        return account

    def get_start_time_value(self):
        if self.start_time:
            date_start, time_start = split_datetime(self.start_time)
            return date_start, time_start
        return None, None

    @property
    def time_start(self):
        _, time_start = self.get_start_time_value()
        return time_start

    @property
    def date_start(self):
        date_start, _ = self.get_start_time_value()
        return date_start

    def get_end_time_value(self):
        if self.end_time:
            date_end, time_end = split_datetime(self.end_time)
            return date_end, time_end
        return None, None

    @property
    def time_end(self):
        _, time_end = self.get_end_time_value()
        return time_end

    @property
    def date_end(self):
        date_end, _ = self.get_end_time_value()
        return date_end


class Answer(Document):
    '''
    测试
    :param id: 答案ID
    :param account_id: 用户ID
    :param test_id: 测试 id
    :param score: 分数
    :param status: 测试状态(pending|finished)
    :param created_time: 开始答题时间
    :param updated_time: 最后答题时间
    :param answers: 答案 {question_id: [options]}
    '''

    STATUS_FINISHED = 'finished'
    STATUS_PENDING = 'pending'

    id = ObjectIdField(primary_key=True)
    test_id = StringField(required=True)
    account_id = StringField(required=True)
    score = IntField(default=0)
    answers = DictField(default={})
    status = StringField(required=True, default=STATUS_PENDING)
    created_time = DateTimeField(default=datetime.utcnow())
    updated_time = DateTimeField()

    meta = {
        "collection_name": 'answer',
        'indexes': [
            ('account_id', 'status', '-score'),
            ('account_id', 'status', '-updated_time'),
        ]
    }
