#! -*- coding: utf-8 -*-
from datetime import datetime

from apis.models import Model


class Test(Model):

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

    __collection__ = 'test'
    __default_fields__ = {
        'status': 'draft',
        'created_time': datetime.utcnow()
    }

    @property
    def creator(self):
        pass


class Question(Model):

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

    __collection__ = 'question'
    __default_fields__ = {
        'created_time': datetime.utcnow()
    }
