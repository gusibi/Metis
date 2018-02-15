# -*- coding: utf-8 -*-

# TODO: datetime support

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###

base_path = '/v1'


DefinitionsAnswersuccess = {'properties': {'ok': {'type': 'boolean'}, 'last': {'type': 'boolean'}}}
DefinitionsAccount = {'required': ['id'], 'properties': {'avatar': {'type': 'string'}, 'nickname': {'type': 'string'}, 'id': {'type': 'string'}}, 'description': 'account 基本信息'}
DefinitionsDistribution = {'properties': {'count': {'type': 'integer', 'format': 'int32'}, 'value': {'type': 'string'}}}
DefinitionsQcosconfig = {'properties': {'sign': {'type': 'string'}}}
DefinitionsOptionwithanswer = {'required': ['option', 'is_checked'], 'properties': {'index': {'type': 'integer', 'format': 'int32'}, 'option': {'type': 'string'}, 'is_checked': {'type': 'boolean'}}}
DefinitionsAuthentications = {'properties': {'wxapp': {'type': 'string'}, 'mobile': {'type': 'string'}}, 'description': '用户详细授权数据'}
DefinitionsNone = {'type': 'object'}
DefinitionsError = {'properties': {'error_code': {'type': 'integer', 'format': 'int32'}, 'text': {'type': 'string'}, 'message': {'type': 'string'}}}
DefinitionsDatetime = {'type': 'string', 'format': 'datetime'}
DefinitionsSuccess = {'properties': {'ok': {'type': 'boolean'}}}
DefinitionsOption = {'required': ['option'], 'properties': {'index': {'type': 'integer', 'format': 'int32'}, 'option': {'type': 'string'}}}
DefinitionsTestscore = {'properties': {'rank': {'type': 'integer'}, 'score': {'type': 'integer'}, 'test_id': {'type': 'string'}}}
DefinitionsAnswerquestion = {'required': ['question_id', 'options'], 'properties': {'question_id': {'type': 'string'}, 'options': {'items': {'type': 'integer', 'format': 'int32'}, 'type': 'array'}}}
DefinitionsAccountdetail = {'required': ['id'], 'properties': {'created_time': DefinitionsDatetime, 'nickname': {'type': 'string'}, 'avatar': {'type': 'string'}, 'username': {'type': 'string'}, 'authentications': DefinitionsAuthentications, 'id': {'type': 'string'}}, 'description': 'account 信息'}
DefinitionsTestingstatistics = {'properties': {'distributions': {'items': DefinitionsDistribution, 'type': 'array'}, 'total_count': {'type': 'integer'}, 'max_score': {'type': 'integer'}, 'min_score': {'type': 'integer'}, 'avg_score': {'type': 'integer'}}}
DefinitionsTestdetail = {'required': ['id', 'title', 'description'], 'properties': {'date_start': {'type': 'string'}, 'description': {'type': 'string'}, 'status': {'type': 'string'}, 'date_end': {'type': 'string'}, 'image': {'type': 'string'}, 'end_time': DefinitionsDatetime, 'question_count': {'type': 'integer'}, 'start_time': DefinitionsDatetime, 'time_start': {'type': 'string'}, 'created_time': DefinitionsDatetime, 'time_end': {'type': 'string'}, 'creator': DefinitionsAccount, 'remark': {'type': 'string'}, 'title': {'type': 'string'}, 'id': {'type': 'string'}}}
DefinitionsUpdatequestion = {'properties': {'type': {'enum': ['single_choice', 'multiple_choice'], 'type': 'string'}, 'title': {'type': 'string'}, 'options': {'items': DefinitionsOptionwithanswer, 'type': 'array'}}}
DefinitionsCreatequestion = {'properties': {'type': {'enum': ['single_choice', 'multiple_choice'], 'type': 'string'}, 'title': {'type': 'string'}, 'options': {'items': DefinitionsOptionwithanswer, 'type': 'array'}}}
DefinitionsCreatetest = {'required': ['title', 'description'], 'properties': {'description': {'maxLength': 256, 'type': 'string', 'minLength': 6}, 'image': {'type': 'string'}, 'end_time': DefinitionsDatetime, 'remark': {'type': 'string'}, 'title': {'maxLength': 128, 'type': 'string', 'minLength': 3}, 'start_time': DefinitionsDatetime}}
DefinitionsTesting = {'required': ['id', 'title', 'description'], 'properties': {'score': {'type': 'integer', 'format': 'int32'}, 'description': {'type': 'string'}, 'image': {'type': 'string'}, 'question_count': {'type': 'integer'}, 'created_time': DefinitionsDatetime, 'creator': DefinitionsAccount, 'title': {'type': 'string'}, 'id': {'type': 'string'}}}
DefinitionsUpdatetest = {'properties': {'description': {'maxLength': 256, 'type': 'string', 'minLength': 6}, 'image': {'type': 'string'}, 'end_time': DefinitionsDatetime, 'remark': {'type': 'string'}, 'title': {'maxLength': 128, 'type': 'string', 'minLength': 3}, 'start_time': DefinitionsDatetime}}
DefinitionsTest = {'required': ['id', 'title', 'description'], 'properties': {'description': {'type': 'string'}, 'image': {'type': 'string'}, 'end_time': DefinitionsDatetime, 'question_count': {'type': 'integer'}, 'start_time': DefinitionsDatetime, 'created_time': DefinitionsDatetime, 'creator': DefinitionsAccount, 'title': {'type': 'string'}, 'id': {'type': 'string'}}}
DefinitionsQuestiondetail = {'required': ['id', 'title', 'options'], 'properties': {'type': {'enum': ['single_choice', 'multiple_choice'], 'type': 'string'}, 'number': {'type': 'integer', 'format': 'int32'}, 'title': {'type': 'string'}, 'options': {'items': DefinitionsOptionwithanswer, 'type': 'array'}, 'id': {'type': 'string'}}}
DefinitionsQuestion = {'required': ['id', 'title', 'options'], 'properties': {'number': {'type': 'integer', 'format': 'int32'}, 'title': {'type': 'string'}, 'options': {'items': DefinitionsOption, 'type': 'array'}, 'id': {'type': 'string'}}}

validators = {
    ('tests_id_statistics', 'GET'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('self_testings', 'GET'): {'args': {'required': [], 'properties': {'limit': {'required': False, 'type': 'integer', 'description': 'limit in query', 'format': 'int32', 'default': 20}, 'offset': {'required': False, 'type': 'integer', 'description': 'offset in query', 'format': 'int32', 'default': 0}}}, 'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('self_tests_id', 'GET'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('self_tests_id', 'DELETE'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('self_tests_id', 'PUT'): {'json': DefinitionsUpdatetest, 'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('tests_id_score', 'GET'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('self_tests_test_id_questions_id', 'PUT'): {'json': DefinitionsUpdatequestion, 'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('self_tests', 'POST'): {'json': DefinitionsCreatetest, 'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('self_tests', 'GET'): {'args': {'required': [], 'properties': {'status': {'required': False, 'type': 'string', 'description': 'test status in query', 'enum': ['draft', 'published', 'withdraw']}, 'offset': {'required': False, 'type': 'integer', 'description': 'offset in query', 'format': 'int32', 'default': 0}, 'limit': {'required': False, 'type': 'integer', 'description': 'limit in query', 'format': 'int32', 'default': 20}}}, 'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('tests_id_questions', 'GET'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('tests_banner', 'GET'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('self_tests_id_publish', 'DELETE'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('self_tests_id_publish', 'PUT'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('tests_id', 'GET'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('self_tests_id_questions', 'POST'): {'json': DefinitionsCreatequestion, 'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('self_tests_id_questions', 'GET'): {'args': {'required': [], 'properties': {'step': {'type': 'integer', 'description': 'step in query', 'format': 'int32', 'default': 0}}}, 'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('qc_cos_config', 'GET'): {'args': {'required': [], 'properties': {'cos_path': {'description': 'cos path', 'required': False, 'type': 'string'}}}, 'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('tests_handpick', 'GET'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('tests_id_answers', 'POST'): {'json': DefinitionsAnswerquestion, 'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
}

filters = {
    ('tests_id_statistics', 'GET'): {200: {'headers': None, 'schema': DefinitionsTestingstatistics}},
    ('self_testings', 'GET'): {200: {'headers': None, 'schema': {'items': DefinitionsTesting, 'type': 'array'}}},
    ('self_tests_id', 'GET'): {200: {'headers': None, 'schema': DefinitionsTestdetail}},
    ('self_tests_id', 'DELETE'): {204: {'headers': None, 'schema': DefinitionsSuccess}},
    ('self_tests_id', 'PUT'): {200: {'headers': None, 'schema': DefinitionsTestdetail}},
    ('tests_id_score', 'GET'): {200: {'headers': None, 'schema': DefinitionsTestscore}},
    ('self_tests_test_id_questions_id', 'PUT'): {200: {'headers': None, 'schema': DefinitionsQuestion}},
    ('self_tests', 'POST'): {201: {'headers': None, 'schema': DefinitionsTestdetail}},
    ('self_tests', 'GET'): {200: {'headers': None, 'schema': {'items': DefinitionsTestdetail, 'type': 'array'}}},
    ('tests_id_questions', 'GET'): {200: {'headers': None, 'schema': {'items': DefinitionsQuestion, 'type': 'array'}}},
    ('tests_banner', 'GET'): {200: {'headers': None, 'schema': {'items': DefinitionsTest, 'type': 'array'}}},
    ('self_tests_id_publish', 'DELETE'): {204: {'headers': None, 'schema': DefinitionsSuccess}},
    ('self_tests_id_publish', 'PUT'): {200: {'headers': None, 'schema': DefinitionsTestdetail}},
    ('tests_id', 'GET'): {200: {'headers': None, 'schema': DefinitionsTest}},
    ('self_tests_id_questions', 'POST'): {201: {'headers': None, 'schema': DefinitionsQuestiondetail}},
    ('self_tests_id_questions', 'GET'): {200: {'headers': None, 'schema': {'items': DefinitionsQuestiondetail, 'type': 'array'}}},
    ('qc_cos_config', 'GET'): {200: {'headers': None, 'schema': DefinitionsQcosconfig}},
    ('tests_handpick', 'GET'): {200: {'headers': None, 'schema': {'items': DefinitionsTest, 'type': 'array'}}},
    ('tests_id_answers', 'POST'): {201: {'headers': None, 'schema': DefinitionsAnswersuccess}},
}

scopes = {
    ('tests_id_statistics', 'GET'): ['open'],
    ('self_testings', 'GET'): ['open'],
    ('self_tests_id', 'GET'): ['open'],
    ('self_tests_id', 'DELETE'): ['open'],
    ('self_tests_id', 'PUT'): ['open'],
    ('tests_id_score', 'GET'): ['open'],
    ('self_tests_test_id_questions_id', 'PUT'): ['open'],
    ('self_tests', 'POST'): ['open'],
    ('self_tests', 'GET'): ['open'],
    ('tests_id_questions', 'GET'): ['open'],
    ('tests_banner', 'GET'): ['open'],
    ('self_tests_id_publish', 'DELETE'): ['open'],
    ('self_tests_id_publish', 'PUT'): ['open'],
    ('tests_id', 'GET'): ['open'],
    ('self_tests_id_questions', 'POST'): ['open'],
    ('self_tests_id_questions', 'GET'): ['open'],
    ('qc_cos_config', 'GET'): ['open'],
    ('tests_handpick', 'GET'): ['open'],
    ('tests_id_answers', 'POST'): ['open'],
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

    import six

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
        if additional_properties_schema:
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
        if not schema:
            return None
        funcs = {
            'object': _normalize_dict,
            'array': _normalize_list,
            'default': _normalize_default,
        }
        type_ = schema.get('type', 'object')
        if not type_ in funcs:
            type_ = 'default'

        return funcs[type_](schema, data)

    return _normalize(schema, data), errors

