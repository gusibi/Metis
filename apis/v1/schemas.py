# -*- coding: utf-8 -*-

# TODO: datetime support

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###

base_path = '/v1'


DefinitionsSuccess = {'properties': {'ok': {'type': 'boolean'}}}
DefinitionsNone = {'type': 'object'}
DefinitionsQcosconfig = {'properties': {'sign': {'type': 'string'}}}
DefinitionsOptionwithanswer = {'required': ['option', 'is_checked'], 'properties': {'index': {'type': 'integer', 'format': 'int32'}, 'option': {'type': 'string'}, 'is_checked': {'type': 'boolean'}}}
DefinitionsDistribution = {'properties': {'value': {'type': 'string'}, 'count': {'type': 'integer', 'format': 'int32'}}}
DefinitionsError = {'properties': {'error_code': {'type': 'integer', 'format': 'int32'}, 'message': {'type': 'string'}, 'text': {'type': 'string'}}}
DefinitionsOption = {'required': ['option'], 'properties': {'index': {'type': 'integer', 'format': 'int32'}, 'option': {'type': 'string'}}}
DefinitionsDatetime = {'type': 'string', 'format': 'datetime'}
DefinitionsTestscore = {'properties': {'test_id': {'type': 'string'}, 'score': {'type': 'integer'}, 'rank': {'type': 'integer'}}}
DefinitionsAnswerquestion = {'required': ['question_id', 'options'], 'properties': {'question_id': {'type': 'string'}, 'options': {'type': 'array', 'items': {'type': 'integer', 'format': 'int32'}}}}
DefinitionsAnswersuccess = {'properties': {'ok': {'type': 'boolean'}, 'last': {'type': 'boolean'}}}
DefinitionsAccount = {'description': 'account 基本信息', 'required': ['id'], 'properties': {'id': {'type': 'string'}, 'nickname': {'type': 'string'}, 'avatar': {'type': 'string'}}}
DefinitionsAuthentications = {'description': '用户详细授权数据', 'properties': {'wxapp': {'type': 'string'}, 'mobile': {'type': 'string'}}}
DefinitionsTestdetail = {'required': ['id', 'title', 'description'], 'properties': {'id': {'type': 'string'}, 'image': {'type': 'string'}, 'title': {'type': 'string'}, 'description': {'type': 'string'}, 'date_start': {'type': 'string'}, 'date_end': {'type': 'string'}, 'time_start': {'type': 'string'}, 'time_end': {'type': 'string'}, 'status': {'type': 'string'}, 'start_time': {'type': 'string', 'format': 'datetime'}, 'end_time': {'type': 'string', 'format': 'datetime'}, 'remark': {'type': 'string'}, 'question_count': {'type': 'integer'}, 'creator': {'description': 'account 基本信息', 'required': ['id'], 'properties': {'id': {'type': 'string'}, 'nickname': {'type': 'string'}, 'avatar': {'type': 'string'}}}, 'created_time': {'type': 'string', 'format': 'datetime'}}}
DefinitionsCreatequestion = {'properties': {'title': {'type': 'string'}, 'type': {'type': 'string', 'enum': ['single_choice', 'multiple_choice']}, 'options': {'type': 'array', 'items': {'required': ['option', 'is_checked'], 'properties': {'index': {'type': 'integer', 'format': 'int32'}, 'option': {'type': 'string'}, 'is_checked': {'type': 'boolean'}}}}}}
DefinitionsAccountdetail = {'description': 'account 信息', 'required': ['id'], 'properties': {'id': {'type': 'string'}, 'username': {'type': 'string'}, 'nickname': {'type': 'string'}, 'avatar': {'type': 'string'}, 'authentications': {'description': '用户详细授权数据', 'properties': {'wxapp': {'type': 'string'}, 'mobile': {'type': 'string'}}}, 'created_time': {'type': 'string', 'format': 'datetime'}}}
DefinitionsTest = {'required': ['id', 'title', 'description'], 'properties': {'id': {'type': 'string'}, 'image': {'type': 'string'}, 'title': {'type': 'string'}, 'description': {'type': 'string'}, 'start_time': {'type': 'string', 'format': 'datetime'}, 'end_time': {'type': 'string', 'format': 'datetime'}, 'question_count': {'type': 'integer'}, 'creator': {'description': 'account 基本信息', 'required': ['id'], 'properties': {'id': {'type': 'string'}, 'nickname': {'type': 'string'}, 'avatar': {'type': 'string'}}}, 'created_time': {'type': 'string', 'format': 'datetime'}}}
DefinitionsTesting = {'required': ['id', 'title', 'description'], 'properties': {'id': {'type': 'string'}, 'score': {'type': 'integer', 'format': 'int32'}, 'image': {'type': 'string'}, 'title': {'type': 'string'}, 'description': {'type': 'string'}, 'question_count': {'type': 'integer'}, 'creator': {'description': 'account 基本信息', 'required': ['id'], 'properties': {'id': {'type': 'string'}, 'nickname': {'type': 'string'}, 'avatar': {'type': 'string'}}}, 'created_time': {'type': 'string', 'format': 'datetime'}}}
DefinitionsUpdatequestion = {'properties': {'title': {'type': 'string'}, 'type': {'type': 'string', 'enum': ['single_choice', 'multiple_choice']}, 'options': {'type': 'array', 'items': {'required': ['option', 'is_checked'], 'properties': {'index': {'type': 'integer', 'format': 'int32'}, 'option': {'type': 'string'}, 'is_checked': {'type': 'boolean'}}}}}}
DefinitionsCreatetest = {'required': ['title', 'description'], 'properties': {'image': {'type': 'string'}, 'title': {'type': 'string', 'minLength': 3, 'maxLength': 128}, 'description': {'type': 'string', 'minLength': 6, 'maxLength': 256}, 'start_time': {'type': 'string', 'format': 'datetime'}, 'end_time': {'type': 'string', 'format': 'datetime'}, 'remark': {'type': 'string'}}}
DefinitionsUpdatetest = {'properties': {'image': {'type': 'string'}, 'title': {'type': 'string', 'minLength': 3, 'maxLength': 128}, 'description': {'type': 'string', 'minLength': 6, 'maxLength': 256}, 'remark': {'type': 'string'}, 'start_time': {'type': 'string', 'format': 'datetime'}, 'end_time': {'type': 'string', 'format': 'datetime'}}}
DefinitionsQuestiondetail = {'required': ['id', 'title', 'options'], 'properties': {'id': {'type': 'string'}, 'title': {'type': 'string'}, 'type': {'type': 'string', 'enum': ['single_choice', 'multiple_choice']}, 'number': {'type': 'integer', 'format': 'int32'}, 'options': {'type': 'array', 'items': {'required': ['option', 'is_checked'], 'properties': {'index': {'type': 'integer', 'format': 'int32'}, 'option': {'type': 'string'}, 'is_checked': {'type': 'boolean'}}}}}}
DefinitionsTestingstatistics = {'properties': {'total_count': {'type': 'integer'}, 'max_score': {'type': 'integer'}, 'min_score': {'type': 'integer'}, 'avg_score': {'type': 'integer'}, 'distributions': {'type': 'array', 'items': {'properties': {'value': {'type': 'string'}, 'count': {'type': 'integer', 'format': 'int32'}}}}}}
DefinitionsQuestion = {'required': ['id', 'title', 'options'], 'properties': {'id': {'type': 'string'}, 'title': {'type': 'string'}, 'number': {'type': 'integer', 'format': 'int32'}, 'options': {'type': 'array', 'items': {'required': ['option'], 'properties': {'index': {'type': 'integer', 'format': 'int32'}, 'option': {'type': 'string'}}}}}}

validators = {
    ('self_tests', 'GET'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}, 'args': {'required': [], 'properties': {'status': {'description': 'test status in query', 'type': 'string', 'required': False, 'enum': ['draft', 'published', 'withdraw']}, 'offset': {'description': 'offset in query', 'type': 'integer', 'format': 'int32', 'default': 0, 'required': False}, 'limit': {'description': 'limit in query', 'type': 'integer', 'format': 'int32', 'default': 20, 'required': False}}}},
    ('self_tests', 'POST'): {'json': {'required': ['title', 'description'], 'properties': {'image': {'type': 'string'}, 'title': {'type': 'string', 'minLength': 3, 'maxLength': 128}, 'description': {'type': 'string', 'minLength': 6, 'maxLength': 256}, 'start_time': {'type': 'string', 'format': 'datetime'}, 'end_time': {'type': 'string', 'format': 'datetime'}, 'remark': {'type': 'string'}}}, 'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('self_tests_id', 'GET'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('self_tests_id', 'PUT'): {'json': {'properties': {'image': {'type': 'string'}, 'title': {'type': 'string', 'minLength': 3, 'maxLength': 128}, 'description': {'type': 'string', 'minLength': 6, 'maxLength': 256}, 'remark': {'type': 'string'}, 'start_time': {'type': 'string', 'format': 'datetime'}, 'end_time': {'type': 'string', 'format': 'datetime'}}}, 'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('self_tests_id', 'DELETE'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('self_tests_id_publish', 'PUT'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('self_tests_id_publish', 'DELETE'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('self_tests_id_questions', 'GET'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}, 'args': {'required': [], 'properties': {'step': {'description': 'step in query', 'type': 'integer', 'format': 'int32', 'default': 0}}}},
    ('self_tests_id_questions', 'POST'): {'json': {'properties': {'title': {'type': 'string'}, 'type': {'type': 'string', 'enum': ['single_choice', 'multiple_choice']}, 'options': {'type': 'array', 'items': {'required': ['option', 'is_checked'], 'properties': {'index': {'type': 'integer', 'format': 'int32'}, 'option': {'type': 'string'}, 'is_checked': {'type': 'boolean'}}}}}}, 'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('self_tests_test_id_questions_id', 'PUT'): {'json': {'properties': {'title': {'type': 'string'}, 'type': {'type': 'string', 'enum': ['single_choice', 'multiple_choice']}, 'options': {'type': 'array', 'items': {'required': ['option', 'is_checked'], 'properties': {'index': {'type': 'integer', 'format': 'int32'}, 'option': {'type': 'string'}, 'is_checked': {'type': 'boolean'}}}}}}, 'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('self_testings', 'GET'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}, 'args': {'required': [], 'properties': {'offset': {'description': 'offset in query', 'type': 'integer', 'format': 'int32', 'default': 0, 'required': False}, 'limit': {'description': 'limit in query', 'type': 'integer', 'format': 'int32', 'default': 20, 'required': False}}}},
    ('tests_banner', 'GET'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('tests_handpick', 'GET'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('tests_id', 'GET'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('tests_id_questions', 'GET'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('tests_id_score', 'GET'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('tests_id_answers', 'POST'): {'json': {'required': ['question_id', 'options'], 'properties': {'question_id': {'type': 'string'}, 'options': {'type': 'array', 'items': {'type': 'integer', 'format': 'int32'}}}}, 'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('tests_id_statistics', 'GET'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('qc_cos_config', 'GET'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}, 'args': {'required': [], 'properties': {'cos_path': {'description': 'cos path', 'type': 'string', 'required': False}}}},
}

filters = {
    ('self_tests', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': {'required': ['id', 'title', 'description'], 'properties': {'id': {'type': 'string'}, 'image': {'type': 'string'}, 'title': {'type': 'string'}, 'description': {'type': 'string'}, 'date_start': {'type': 'string'}, 'date_end': {'type': 'string'}, 'time_start': {'type': 'string'}, 'time_end': {'type': 'string'}, 'status': {'type': 'string'}, 'start_time': {'type': 'string', 'format': 'datetime'}, 'end_time': {'type': 'string', 'format': 'datetime'}, 'remark': {'type': 'string'}, 'question_count': {'type': 'integer'}, 'creator': {'description': 'account 基本信息', 'required': ['id'], 'properties': {'id': {'type': 'string'}, 'nickname': {'type': 'string'}, 'avatar': {'type': 'string'}}}, 'created_time': {'type': 'string', 'format': 'datetime'}}}}}},
    ('self_tests', 'POST'): {201: {'headers': None, 'schema': {'required': ['id', 'title', 'description'], 'properties': {'id': {'type': 'string'}, 'image': {'type': 'string'}, 'title': {'type': 'string'}, 'description': {'type': 'string'}, 'date_start': {'type': 'string'}, 'date_end': {'type': 'string'}, 'time_start': {'type': 'string'}, 'time_end': {'type': 'string'}, 'status': {'type': 'string'}, 'start_time': {'type': 'string', 'format': 'datetime'}, 'end_time': {'type': 'string', 'format': 'datetime'}, 'remark': {'type': 'string'}, 'question_count': {'type': 'integer'}, 'creator': {'description': 'account 基本信息', 'required': ['id'], 'properties': {'id': {'type': 'string'}, 'nickname': {'type': 'string'}, 'avatar': {'type': 'string'}}}, 'created_time': {'type': 'string', 'format': 'datetime'}}}}},
    ('self_tests_id', 'GET'): {200: {'headers': None, 'schema': {'required': ['id', 'title', 'description'], 'properties': {'id': {'type': 'string'}, 'image': {'type': 'string'}, 'title': {'type': 'string'}, 'description': {'type': 'string'}, 'date_start': {'type': 'string'}, 'date_end': {'type': 'string'}, 'time_start': {'type': 'string'}, 'time_end': {'type': 'string'}, 'status': {'type': 'string'}, 'start_time': {'type': 'string', 'format': 'datetime'}, 'end_time': {'type': 'string', 'format': 'datetime'}, 'remark': {'type': 'string'}, 'question_count': {'type': 'integer'}, 'creator': {'description': 'account 基本信息', 'required': ['id'], 'properties': {'id': {'type': 'string'}, 'nickname': {'type': 'string'}, 'avatar': {'type': 'string'}}}, 'created_time': {'type': 'string', 'format': 'datetime'}}}}},
    ('self_tests_id', 'PUT'): {200: {'headers': None, 'schema': {'required': ['id', 'title', 'description'], 'properties': {'id': {'type': 'string'}, 'image': {'type': 'string'}, 'title': {'type': 'string'}, 'description': {'type': 'string'}, 'date_start': {'type': 'string'}, 'date_end': {'type': 'string'}, 'time_start': {'type': 'string'}, 'time_end': {'type': 'string'}, 'status': {'type': 'string'}, 'start_time': {'type': 'string', 'format': 'datetime'}, 'end_time': {'type': 'string', 'format': 'datetime'}, 'remark': {'type': 'string'}, 'question_count': {'type': 'integer'}, 'creator': {'description': 'account 基本信息', 'required': ['id'], 'properties': {'id': {'type': 'string'}, 'nickname': {'type': 'string'}, 'avatar': {'type': 'string'}}}, 'created_time': {'type': 'string', 'format': 'datetime'}}}}},
    ('self_tests_id', 'DELETE'): {204: {'headers': None, 'schema': {'properties': {'ok': {'type': 'boolean'}}}}},
    ('self_tests_id_publish', 'PUT'): {200: {'headers': None, 'schema': {'required': ['id', 'title', 'description'], 'properties': {'id': {'type': 'string'}, 'image': {'type': 'string'}, 'title': {'type': 'string'}, 'description': {'type': 'string'}, 'date_start': {'type': 'string'}, 'date_end': {'type': 'string'}, 'time_start': {'type': 'string'}, 'time_end': {'type': 'string'}, 'status': {'type': 'string'}, 'start_time': {'type': 'string', 'format': 'datetime'}, 'end_time': {'type': 'string', 'format': 'datetime'}, 'remark': {'type': 'string'}, 'question_count': {'type': 'integer'}, 'creator': {'description': 'account 基本信息', 'required': ['id'], 'properties': {'id': {'type': 'string'}, 'nickname': {'type': 'string'}, 'avatar': {'type': 'string'}}}, 'created_time': {'type': 'string', 'format': 'datetime'}}}}},
    ('self_tests_id_publish', 'DELETE'): {204: {'headers': None, 'schema': {'properties': {'ok': {'type': 'boolean'}}}}},
    ('self_tests_id_questions', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': {'required': ['id', 'title', 'options'], 'properties': {'id': {'type': 'string'}, 'title': {'type': 'string'}, 'type': {'type': 'string', 'enum': ['single_choice', 'multiple_choice']}, 'number': {'type': 'integer', 'format': 'int32'}, 'options': {'type': 'array', 'items': {'required': ['option', 'is_checked'], 'properties': {'index': {'type': 'integer', 'format': 'int32'}, 'option': {'type': 'string'}, 'is_checked': {'type': 'boolean'}}}}}}}}},
    ('self_tests_id_questions', 'POST'): {201: {'headers': None, 'schema': {'required': ['id', 'title', 'options'], 'properties': {'id': {'type': 'string'}, 'title': {'type': 'string'}, 'type': {'type': 'string', 'enum': ['single_choice', 'multiple_choice']}, 'number': {'type': 'integer', 'format': 'int32'}, 'options': {'type': 'array', 'items': {'required': ['option', 'is_checked'], 'properties': {'index': {'type': 'integer', 'format': 'int32'}, 'option': {'type': 'string'}, 'is_checked': {'type': 'boolean'}}}}}}}},
    ('self_tests_test_id_questions_id', 'PUT'): {200: {'headers': None, 'schema': {'required': ['id', 'title', 'options'], 'properties': {'id': {'type': 'string'}, 'title': {'type': 'string'}, 'number': {'type': 'integer', 'format': 'int32'}, 'options': {'type': 'array', 'items': {'required': ['option'], 'properties': {'index': {'type': 'integer', 'format': 'int32'}, 'option': {'type': 'string'}}}}}}}},
    ('self_testings', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': {'required': ['id', 'title', 'description'], 'properties': {'id': {'type': 'string'}, 'score': {'type': 'integer', 'format': 'int32'}, 'image': {'type': 'string'}, 'title': {'type': 'string'}, 'description': {'type': 'string'}, 'question_count': {'type': 'integer'}, 'creator': {'description': 'account 基本信息', 'required': ['id'], 'properties': {'id': {'type': 'string'}, 'nickname': {'type': 'string'}, 'avatar': {'type': 'string'}}}, 'created_time': {'type': 'string', 'format': 'datetime'}}}}}},
    ('tests_banner', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': {'required': ['id', 'title', 'description'], 'properties': {'id': {'type': 'string'}, 'image': {'type': 'string'}, 'title': {'type': 'string'}, 'description': {'type': 'string'}, 'start_time': {'type': 'string', 'format': 'datetime'}, 'end_time': {'type': 'string', 'format': 'datetime'}, 'question_count': {'type': 'integer'}, 'creator': {'description': 'account 基本信息', 'required': ['id'], 'properties': {'id': {'type': 'string'}, 'nickname': {'type': 'string'}, 'avatar': {'type': 'string'}}}, 'created_time': {'type': 'string', 'format': 'datetime'}}}}}},
    ('tests_handpick', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': {'required': ['id', 'title', 'description'], 'properties': {'id': {'type': 'string'}, 'image': {'type': 'string'}, 'title': {'type': 'string'}, 'description': {'type': 'string'}, 'start_time': {'type': 'string', 'format': 'datetime'}, 'end_time': {'type': 'string', 'format': 'datetime'}, 'question_count': {'type': 'integer'}, 'creator': {'description': 'account 基本信息', 'required': ['id'], 'properties': {'id': {'type': 'string'}, 'nickname': {'type': 'string'}, 'avatar': {'type': 'string'}}}, 'created_time': {'type': 'string', 'format': 'datetime'}}}}}},
    ('tests_id', 'GET'): {200: {'headers': None, 'schema': {'required': ['id', 'title', 'description'], 'properties': {'id': {'type': 'string'}, 'image': {'type': 'string'}, 'title': {'type': 'string'}, 'description': {'type': 'string'}, 'start_time': {'type': 'string', 'format': 'datetime'}, 'end_time': {'type': 'string', 'format': 'datetime'}, 'question_count': {'type': 'integer'}, 'creator': {'description': 'account 基本信息', 'required': ['id'], 'properties': {'id': {'type': 'string'}, 'nickname': {'type': 'string'}, 'avatar': {'type': 'string'}}}, 'created_time': {'type': 'string', 'format': 'datetime'}}}}},
    ('tests_id_questions', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': {'required': ['id', 'title', 'options'], 'properties': {'id': {'type': 'string'}, 'title': {'type': 'string'}, 'number': {'type': 'integer', 'format': 'int32'}, 'options': {'type': 'array', 'items': {'required': ['option'], 'properties': {'index': {'type': 'integer', 'format': 'int32'}, 'option': {'type': 'string'}}}}}}}}},
    ('tests_id_score', 'GET'): {200: {'headers': None, 'schema': {'properties': {'test_id': {'type': 'string'}, 'score': {'type': 'integer'}, 'rank': {'type': 'integer'}}}}},
    ('tests_id_answers', 'POST'): {201: {'headers': None, 'schema': {'properties': {'ok': {'type': 'boolean'}, 'last': {'type': 'boolean'}}}}},
    ('tests_id_statistics', 'GET'): {200: {'headers': None, 'schema': {'properties': {'total_count': {'type': 'integer'}, 'max_score': {'type': 'integer'}, 'min_score': {'type': 'integer'}, 'avg_score': {'type': 'integer'}, 'distributions': {'type': 'array', 'items': {'properties': {'value': {'type': 'string'}, 'count': {'type': 'integer', 'format': 'int32'}}}}}}}},
    ('qc_cos_config', 'GET'): {200: {'headers': None, 'schema': {'properties': {'sign': {'type': 'string'}}}}},
}

scopes = {
    ('self_tests', 'GET'): ['open'],
    ('self_tests', 'POST'): ['open'],
    ('self_tests_id', 'GET'): ['open'],
    ('self_tests_id', 'PUT'): ['open'],
    ('self_tests_id', 'DELETE'): ['open'],
    ('self_tests_id_publish', 'PUT'): ['open'],
    ('self_tests_id_publish', 'DELETE'): ['open'],
    ('self_tests_id_questions', 'GET'): ['open'],
    ('self_tests_id_questions', 'POST'): ['open'],
    ('self_tests_test_id_questions_id', 'PUT'): ['open'],
    ('self_testings', 'GET'): ['open'],
    ('tests_banner', 'GET'): ['open'],
    ('tests_handpick', 'GET'): ['open'],
    ('tests_id', 'GET'): ['open'],
    ('tests_id_questions', 'GET'): ['open'],
    ('tests_id_score', 'GET'): ['open'],
    ('tests_id_answers', 'POST'): ['open'],
    ('tests_id_statistics', 'GET'): ['open'],
    ('qc_cos_config', 'GET'): ['open'],
}


class Current(object):

    request = None


current = Current()


class Security(object):

    def __init__(self):
        super(Security, self).__init__()
        self._loader = lambda x: []

    @property
    def scopes(self):
        return self._loader(current.request)

    def scopes_loader(self, func):
        self._loader = func
        return func

security = Security()


def merge_default(schema, value, get_first=True):
    # TODO: more types support
    type_defaults = {
        'integer': 9573,
        'string': 'something',
        'object': {},
        'array': [],
        'boolean': False
    }

    results = normalize(schema, value, type_defaults)
    if get_first:
        return results[0]
    return results


def normalize(schema, data, required_defaults=None):
    if required_defaults is None:
        required_defaults = {}
    errors = []

    class DataWrapper(object):

        def __init__(self, data):
            super(DataWrapper, self).__init__()
            self.data = data

        def get(self, key, default=None):
            if isinstance(self.data, dict):
                return self.data.get(key, default)
            return getattr(self.data, key, default)

        def has(self, key):
            if isinstance(self.data, dict):
                return key in self.data
            return hasattr(self.data, key)

        def keys(self):
            if isinstance(self.data, dict):
                return list(self.data.keys())
            return list(getattr(self.data, '__dict__', {}).keys())

        def get_check(self, key, default=None):
            if isinstance(self.data, dict):
                value = self.data.get(key, default)
                has_key = key in self.data
            else:
                try:
                    value = getattr(self.data, key)
                except AttributeError:
                    value = default
                    has_key = False
                else:
                    has_key = True
            return value, has_key

    def _merge_dict(src, dst):
        for k, v in six.iteritems(dst):
            if isinstance(src, dict):
                if isinstance(v, dict):
                    r = _merge_dict(src.get(k, {}), v)
                    src[k] = r
                else:
                    src[k] = v
            else:
                src = {k: v}
        return src

    def _normalize_dict(schema, data):
        result = {}
        if not isinstance(data, DataWrapper):
            data = DataWrapper(data)

        for _schema in schema.get('allOf', []):
            rs_component = _normalize(_schema, data)
            _merge_dict(result, rs_component)

        for key, _schema in six.iteritems(schema.get('properties', {})):
            # set default
            type_ = _schema.get('type', 'object')

            # get value
            value, has_key = data.get_check(key)
            if has_key:
                result[key] = _normalize(_schema, value)
            elif 'default' in _schema:
                result[key] = _schema['default']
            elif key in schema.get('required', []):
                if type_ in required_defaults:
                    result[key] = required_defaults[type_]
                else:
                    errors.append(dict(name='property_missing',
                                       message='`%s` is required' % key))

        additional_properties_schema = schema.get('additionalProperties', False)
        if additional_properties_schema is not False:
            aproperties_set = set(data.keys()) - set(result.keys())
            for pro in aproperties_set:
                result[pro] = _normalize(additional_properties_schema, data.get(pro))

        return result

    def _normalize_list(schema, data):
        result = []
        if hasattr(data, '__iter__') and not isinstance(data, dict):
            for item in data:
                result.append(_normalize(schema.get('items'), item))
        elif 'default' in schema:
            result = schema['default']
        return result

    def _normalize_default(schema, data):
        if data is None:
            return schema.get('default')
        else:
            return data

    def _normalize(schema, data):
        if schema is True or schema == {}:
            return data
        if not schema:
            return None
        funcs = {
            'object': _normalize_dict,
            'array': _normalize_list,
            'default': _normalize_default,
        }
        type_ = schema.get('type', 'object')
        if type_ not in funcs:
            type_ = 'default'

        return funcs[type_](schema, data)

    return _normalize(schema, data), errors

