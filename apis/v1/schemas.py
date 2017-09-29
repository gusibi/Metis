# -*- coding: utf-8 -*-

# TODO: datetime support

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###

base_path = '/v1'


DefinitionsAccount = {'properties': {'id': {'type': 'string'}, 'avatar': {'type': 'string'}, 'nickname': {'type': 'string'}}, 'required': ['id'], 'description': 'account 基本信息'}
DefinitionsQcosconfig = {'properties': {'sign': {'type': 'string'}}}
DefinitionsOption = {'properties': {'index': {'format': 'int32', 'type': 'integer'}, 'option': {'type': 'string'}}, 'required': ['option']}
DefinitionsAnswersuccess = {'properties': {'ok': {'type': 'boolean'}, 'last': {'type': 'boolean'}}}
DefinitionsAuthentications = {'properties': {'mobile': {'type': 'string'}, 'wxapp': {'type': 'string'}}, 'description': '用户详细授权数据'}
DefinitionsSuccess = {'properties': {'ok': {'type': 'boolean'}}}
DefinitionsError = {'properties': {'message': {'type': 'string'}, 'error_code': {'format': 'int32', 'type': 'integer'}, 'text': {'type': 'string'}}}
DefinitionsNone = {'type': 'object'}
DefinitionsAnswerquestion = {'properties': {'options': {'items': {'format': 'int32', 'type': 'integer'}, 'type': 'array'}, 'question_id': {'type': 'string'}}, 'required': ['question_id', 'options']}
DefinitionsDistribution = {'properties': {'count': {'format': 'int32', 'type': 'integer'}, 'value': {'type': 'string'}}}
DefinitionsOptionwithanswer = {'properties': {'is_checked': {'type': 'boolean'}, 'index': {'format': 'int32', 'type': 'integer'}, 'option': {'type': 'string'}}, 'required': ['option', 'is_checked']}
DefinitionsDatetime = {'format': 'datetime', 'type': 'string'}
DefinitionsTestscore = {'properties': {'score': {'type': 'integer'}, 'test_id': {'type': 'string'}, 'rank': {'type': 'integer'}}}
DefinitionsTestingstatistics = {'properties': {'distributions': {'items': DefinitionsDistribution, 'type': 'array'}, 'min_score': {'type': 'integer'}, 'avg_score': {'type': 'integer'}, 'max_score': {'type': 'integer'}, 'total_count': {'type': 'integer'}}}
DefinitionsQuestion = {'properties': {'number': {'format': 'int32', 'type': 'integer'}, 'id': {'type': 'string'}, 'title': {'type': 'string'}, 'options': {'items': DefinitionsOption, 'type': 'array'}}, 'required': ['id', 'title', 'options']}
DefinitionsUpdatequestion = {'properties': {'options': {'items': DefinitionsOptionwithanswer, 'type': 'array'}, 'type': {'enum': ['single_choice', 'multiple_choice'], 'type': 'string'}, 'title': {'type': 'string'}}}
DefinitionsUpdatetest = {'properties': {'start_time': DefinitionsDatetime, 'status': {'enum': ['published', 'withdraw'], 'type': 'string'}, 'end_time': DefinitionsDatetime, 'title': {'type': 'string', 'minLength': 8, 'maxLength': 128}, 'image': {'type': 'string'}, 'description': {'type': 'string', 'minLength': 16, 'maxLength': 256}, 'remark': {'type': 'string'}}}
DefinitionsCreatequestion = {'properties': {'options': {'items': DefinitionsOptionwithanswer, 'type': 'array'}, 'type': {'enum': ['single_choice', 'multiple_choice'], 'type': 'string'}, 'title': {'type': 'string'}}}
DefinitionsTestdetail = {'properties': {'date_end': {'type': 'string'}, 'time_start': {'type': 'string'}, 'end_time': DefinitionsDatetime, 'image': {'type': 'string'}, 'date_start': {'type': 'string'}, 'start_time': DefinitionsDatetime, 'status': {'type': 'string'}, 'time_end': {'type': 'string'}, 'creator': DefinitionsAccount, 'title': {'type': 'string'}, 'question_count': {'type': 'integer'}, 'id': {'type': 'string'}, 'description': {'type': 'string'}, 'remark': {'type': 'string'}, 'created_time': DefinitionsDatetime}, 'required': ['id', 'title', 'description']}
DefinitionsTesting = {'properties': {'creator': DefinitionsAccount, 'image': {'type': 'string'}, 'created_time': DefinitionsDatetime, 'title': {'type': 'string'}, 'score': {'format': 'int32', 'type': 'integer'}, 'id': {'type': 'string'}, 'description': {'type': 'string'}, 'question_count': {'type': 'integer'}}, 'required': ['id', 'score', 'title', 'description']}
DefinitionsCreatetest = {'properties': {'start_time': DefinitionsDatetime, 'end_time': DefinitionsDatetime, 'title': {'type': 'string', 'minLength': 8, 'maxLength': 128}, 'image': {'type': 'string'}, 'description': {'type': 'string', 'minLength': 16, 'maxLength': 256}, 'remark': {'type': 'string'}}, 'required': ['title', 'description']}
DefinitionsQuestiondetail = {'properties': {'number': {'format': 'int32', 'type': 'integer'}, 'id': {'type': 'string'}, 'type': {'enum': ['single_choice', 'multiple_choice'], 'type': 'string'}, 'title': {'type': 'string'}, 'options': {'items': DefinitionsOptionwithanswer, 'type': 'array'}}, 'required': ['id', 'title', 'options']}
DefinitionsAccountdetail = {'properties': {'username': {'type': 'string'}, 'avatar': {'type': 'string'}, 'nickname': {'type': 'string'}, 'id': {'type': 'string'}, 'authentications': DefinitionsAuthentications, 'created_time': DefinitionsDatetime}, 'required': ['id'], 'description': 'account 信息'}
DefinitionsTest = {'properties': {'creator': DefinitionsAccount, 'end_time': DefinitionsDatetime, 'image': {'type': 'string'}, 'start_time': DefinitionsDatetime, 'created_time': DefinitionsDatetime, 'title': {'type': 'string'}, 'id': {'type': 'string'}, 'description': {'type': 'string'}, 'question_count': {'type': 'integer'}}, 'required': ['id', 'title', 'description']}

validators = {
    ('self_tests', 'GET'): {'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}, 'args': {'properties': {'status': {'required': False, 'enum': ['draft', 'published', 'withdraw'], 'description': 'test status in query', 'type': 'string'}, 'limit': {'required': False, 'format': 'int32', 'default': 20, 'description': 'limit in query', 'type': 'integer'}, 'offset': {'required': False, 'format': 'int32', 'default': 0, 'description': 'offset in query', 'type': 'integer'}}, 'required': []}},
    ('self_tests', 'POST'): {'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}, 'json': DefinitionsCreatetest},
    ('tests_id_questions', 'GET'): {'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('tests_id_score', 'GET'): {'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('self_testings', 'GET'): {'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}, 'args': {'properties': {'limit': {'required': False, 'format': 'int32', 'default': 20, 'description': 'limit in query', 'type': 'integer'}, 'offset': {'required': False, 'format': 'int32', 'default': 0, 'description': 'offset in query', 'type': 'integer'}}, 'required': []}},
    ('tests_id_answers', 'POST'): {'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}, 'json': DefinitionsAnswerquestion},
    ('self_tests_id_questions', 'GET'): {'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}, 'args': {'properties': {'step': {'format': 'int32', 'default': 0, 'description': 'step in query', 'type': 'integer'}}, 'required': []}},
    ('self_tests_id_questions', 'POST'): {'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}, 'json': DefinitionsCreatequestion},
    ('tests_id', 'GET'): {'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('self_tests_test_id_questions_id', 'PUT'): {'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}, 'json': DefinitionsUpdatequestion},
    ('tests_handpick', 'GET'): {'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('self_tests_id', 'GET'): {'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('self_tests_id', 'DELETE'): {'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('self_tests_id', 'PUT'): {'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}, 'json': DefinitionsUpdatetest},
    ('tests_id_statistics', 'GET'): {'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('qc_cos_config', 'GET'): {'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}, 'args': {'properties': {'cos_path': {'description': 'cos path', 'type': 'string', 'required': False}}, 'required': []}},
}

filters = {
    ('self_tests', 'GET'): {200: {'headers': None, 'schema': {'items': DefinitionsTestdetail, 'type': 'array'}}},
    ('self_tests', 'POST'): {201: {'headers': None, 'schema': DefinitionsTestdetail}},
    ('tests_id_questions', 'GET'): {200: {'headers': None, 'schema': {'items': DefinitionsQuestion, 'type': 'array'}}},
    ('tests_id_score', 'GET'): {200: {'headers': None, 'schema': DefinitionsTestscore}},
    ('self_testings', 'GET'): {200: {'headers': None, 'schema': {'items': DefinitionsTesting, 'type': 'array'}}},
    ('tests_id_answers', 'POST'): {201: {'headers': None, 'schema': DefinitionsAnswersuccess}},
    ('self_tests_id_questions', 'GET'): {200: {'headers': None, 'schema': {'items': DefinitionsQuestiondetail, 'type': 'array'}}},
    ('self_tests_id_questions', 'POST'): {201: {'headers': None, 'schema': DefinitionsQuestiondetail}},
    ('tests_id', 'GET'): {200: {'headers': None, 'schema': DefinitionsTest}},
    ('self_tests_test_id_questions_id', 'PUT'): {200: {'headers': None, 'schema': DefinitionsQuestion}},
    ('tests_handpick', 'GET'): {200: {'headers': None, 'schema': {'items': DefinitionsTest, 'type': 'array'}}},
    ('self_tests_id', 'GET'): {200: {'headers': None, 'schema': DefinitionsTestdetail}},
    ('self_tests_id', 'DELETE'): {204: {'headers': None, 'schema': DefinitionsSuccess}},
    ('self_tests_id', 'PUT'): {200: {'headers': None, 'schema': DefinitionsTest}},
    ('tests_id_statistics', 'GET'): {200: {'headers': None, 'schema': DefinitionsTestingstatistics}},
    ('qc_cos_config', 'GET'): {200: {'headers': None, 'schema': DefinitionsQcosconfig}},
}

scopes = {
    ('self_tests', 'GET'): ['open'],
    ('self_tests', 'POST'): ['open'],
    ('tests_id_questions', 'GET'): ['open'],
    ('tests_id_score', 'GET'): ['open'],
    ('self_testings', 'GET'): ['open'],
    ('tests_id_answers', 'POST'): ['open'],
    ('self_tests_id_questions', 'GET'): ['open'],
    ('self_tests_id_questions', 'POST'): ['open'],
    ('tests_id', 'GET'): ['open'],
    ('self_tests_test_id_questions_id', 'PUT'): ['open'],
    ('tests_handpick', 'GET'): ['open'],
    ('self_tests_id', 'GET'): ['open'],
    ('self_tests_id', 'DELETE'): ['open'],
    ('self_tests_id', 'PUT'): ['open'],
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

