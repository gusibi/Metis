#! -*- coding: utf-8 -*-
from datetime import datetime

from apis.models import Model


class Choice(Model):

    '''
    选择题
    :param _id: 测试ID
    :param creator_id: 用户ID
    :param title: 金额 精确到分
    :param questions: 问题
                [
                    {
                        'question': 'title',
                        'choices': [1, 2, 3, 4],
                        'answers': [1, 2],
                    },
                ]
    :param remark: 备注
    :param start_time: 开始时间
    :param end_time: 结束时间
    :param status: 状态(草稿|发布|下线)
    :param created_time: 创建时间
    '''

    __collection__ = 'choice'
    __default_fields__ = {
        'created_time': datetime.utcnow()
    }
