#! -*- coding: utf-8 -*-
from datetime import datetime

from pymongo import TEXT, DESCENDING, ASCENDING
from pymongo.operations import IndexModel
from pymodm import MongoModel, EmbeddedMongoModel, fields


class Question(EmbeddedMongoModel):

    '''
    题目：
    :param _id: 问题 ID
    :param title: 题目
    :param test_id:  所属测试 ID
    :param type: 题目类型 'single_choice|multiple_choice'
    :param options: 选项
                [
                {'value': '这是第一个选项', 'is_checked': True},
                {'value': '这是第二个选项', 'is_checked': False},
                ]
    :param index: 1,
    '''

    collection_name = 'question'

    id = fields.ObjectIdField(primary_key=True, required=True)
    title = fields.CharField(required=True)
    type = fields.CharField(required=True, default='single_choice')
    number = fields.IntegerField(required=True, default=0)
    options = fields.ListField(required=True, default=[])
    created_time = fields.DateTimeField(default=datetime.utcnow())
    updated_time = fields.DateTimeField()



class Test(MongoModel):

    '''
    测试
    :param _id: 测试ID
    :param creator_id: 用户ID
    :param title: 测试 title
    :param description: 测试描述
    :param remark: 备注
    :param start_time: 开始时间
    :param end_time: 结束时间
    :param status: 状态(草稿|发布|下线)
    :param created_time: 创建时间
    '''

    collection_name = 'test'

    id = fields.ObjectIdField(primary_key=True, required=True)
    creator_id = fields.ObjectIdField(required=True)
    title = fields.CharField(required=True)
    description = fields.CharField(required=True)
    remark = fields.CharField()
    status = fields.CharField(required=True, default='draft')
    total_score = fields.IntegerField()
    participate_number = fields.IntegerField(required=True, default=0)
    start_time = fields.DateTimeField()
    end_time = fields.DateTimeField()
    created_time = fields.DateTimeField(default=datetime.utcnow())
    updated_time = fields.DateTimeField()
    questions = fields.EmbeddedDocumentListField(Question, default=[])

    class Meta:
        # Text index on title can be used for text search.
        indexes = [
            IndexModel([('title', TEXT)]),
            IndexModel([('creator_id', TEXT),
                        ('status', TEXT)]),
            IndexModel([('participate_number', DESCENDING),
                        ('status', TEXT)], name='participate_status')
        ]

    @property
    def creator(self):
        pass


