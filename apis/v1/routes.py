# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.self_tests import SelfTests
from .api.self_tests_id import SelfTestsId
from .api.self_tests_id_questions import SelfTestsIdQuestions
from .api.self_tests_test_id_questions_id import SelfTestsTestIdQuestionsId
from .api.self_testings import SelfTestings
from .api.tests_handpick import TestsHandpick
from .api.tests_id import TestsId
from .api.tests_id_questions import TestsIdQuestions
from .api.tests_id_score import TestsIdScore
from .api.tests_id_answers import TestsIdAnswers
from .api.tests_id_statistics import TestsIdStatistics
from .api.qc_cos_config import QcCosConfig


routes = [
    dict(resource=SelfTests.as_view(), urls=['/self/tests'], endpoint='self_tests'),
    dict(resource=SelfTestsId.as_view(), urls=['/self/tests/<id>'], endpoint='self_tests_id'),
    dict(resource=SelfTestsIdQuestions.as_view(), urls=['/self/tests/<id>/questions'], endpoint='self_tests_id_questions'),
    dict(resource=SelfTestsTestIdQuestionsId.as_view(), urls=['/self/tests/<test_id>/questions/<id>'], endpoint='self_tests_test_id_questions_id'),
    dict(resource=SelfTestings.as_view(), urls=['/self/testings'], endpoint='self_testings'),
    dict(resource=TestsHandpick.as_view(), urls=['/tests/handpick'], endpoint='tests_handpick'),
    dict(resource=TestsId.as_view(), urls=['/tests/<id>'], endpoint='tests_id'),
    dict(resource=TestsIdQuestions.as_view(), urls=['/tests/<id>/questions'], endpoint='tests_id_questions'),
    dict(resource=TestsIdScore.as_view(), urls=['/tests/<id>/score'], endpoint='tests_id_score'),
    dict(resource=TestsIdAnswers.as_view(), urls=['/tests/<id>/answers'], endpoint='tests_id_answers'),
    dict(resource=TestsIdStatistics.as_view(), urls=['/tests/<id>/statistics'], endpoint='tests_id_statistics'),
    dict(resource=QcCosConfig.as_view(), urls=['/qc_cos/config'], endpoint='qc_cos_config'),
]