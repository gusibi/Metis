# -*- coding: utf-8 -*-

# TODO: datetime support

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###

base_path = '/v1'


DefinitionsQcosconfig = {'properties': {'sign': {'type': 'string'}}}
DefinitionsNone = {'type': 'object'}
DefinitionsError = {'properties': {'error_code': {'type': 'integer', 'format': 'int32'}, 'text': {'type': 'string'}, 'message': {'type': 'string'}}}
DefinitionsSuccess = {'properties': {'ok': {'type': 'boolean'}}}
DefinitionsAnswerquestion = {'properties': {'options': {'type': 'array', 'items': {'type': 'integer', 'format': 'int32'}}, 'question_id': {'type': 'string'}}, 'required': ['question_id', 'options']}
DefinitionsOption = {'properties': {'index': {'type': 'integer', 'format': 'int32'}, 'option': {'type': 'string'}}, 'required': ['option']}
DefinitionsDatetime = {'type': 'string', 'format': 'datetime'}
DefinitionsAnswersuccess = {'properties': {'last': {'type': 'boolean'}, 'ok': {'type': 'boolean'}}}
DefinitionsDistribution = {'properties': {'value': {'type': 'string'}, 'count': {'type': 'integer', 'format': 'int32'}}}
DefinitionsAccount = {'description': 'account 基本信息', 'properties': {'nickname': {'type': 'string'}, 'id': {'type': 'string'}, 'avatar': {'type': 'string'}}, 'required': ['id']}
DefinitionsAuthentications = {'description': '用户详细授权数据', 'properties': {'wxapp': {'type': 'string'}, 'mobile': {'type': 'string'}}}
DefinitionsOptionwithanswer = {'properties': {'index': {'type': 'integer', 'format': 'int32'}, 'option': {'type': 'string'}, 'is_checked': {'type': 'boolean'}}, 'required': ['option', 'is_checked']}
DefinitionsUpdatetest = {'properties': {'title': {'type': 'string', 'maxLength': 128, 'minLength': 8}, 'description': {'type': 'string', 'maxLength': 256, 'minLength': 16}, 'status': {'type': 'string', 'enum': ['published', 'withdraw']}, 'image': {'type': 'string'}, 'end_time': DefinitionsDatetime, 'start_time': DefinitionsDatetime, 'remark': {'type': 'string'}}}
DefinitionsAccountdetail = {'description': 'account 信息', 'properties': {'username': {'type': 'string'}, 'authentications': DefinitionsAuthentications, 'nickname': {'type': 'string'}, 'created_time': DefinitionsDatetime, 'avatar': {'type': 'string'}, 'id': {'type': 'string'}}, 'required': ['id']}
DefinitionsTest = {'properties': {'id': {'type': 'string'}, 'description': {'type': 'string'}, 'question_count': {'type': 'integer'}, 'start_time': DefinitionsDatetime, 'created_time': DefinitionsDatetime, 'creator': DefinitionsAccount, 'title': {'type': 'string'}, 'image': {'type': 'string'}, 'end_time': DefinitionsDatetime}, 'required': ['id', 'title', 'description']}
DefinitionsQuestiondetail = {'properties': {'title': {'type': 'string'}, 'type': {'type': 'string', 'enum': ['single_choice', 'multiple_choice']}, 'id': {'type': 'string'}, 'number': {'type': 'integer', 'format': 'int32'}, 'options': {'type': 'array', 'items': DefinitionsOptionwithanswer}}, 'required': ['id', 'title', 'options']}
DefinitionsTesting = {'properties': {'id': {'type': 'string'}, 'description': {'type': 'string'}, 'question_count': {'type': 'integer'}, 'created_time': DefinitionsDatetime, 'score': {'type': 'integer', 'format': 'int32'}, 'creator': DefinitionsAccount, 'image': {'type': 'string'}, 'title': {'type': 'string'}}, 'required': ['id', 'score', 'title', 'description']}
DefinitionsQuestion = {'properties': {'title': {'type': 'string'}, 'id': {'type': 'string'}, 'number': {'type': 'integer', 'format': 'int32'}, 'options': {'type': 'array', 'items': DefinitionsOption}}, 'required': ['id', 'title', 'options']}
DefinitionsTestdetail = {'properties': {'date_start': {'type': 'string'}, 'start_time': DefinitionsDatetime, 'description': {'type': 'string'}, 'status': {'type': 'string'}, 'question_count': {'type': 'integer'}, 'time_end': {'type': 'string'}, 'id': {'type': 'string'}, 'created_time': DefinitionsDatetime, 'date_end': {'type': 'string'}, 'time_start': {'type': 'string'}, 'title': {'type': 'string'}, 'creator': DefinitionsAccount, 'image': {'type': 'string'}, 'end_time': DefinitionsDatetime, 'remark': {'type': 'string'}}, 'required': ['id', 'title', 'description']}
DefinitionsCreatetest = {'properties': {'title': {'type': 'string', 'maxLength': 128, 'minLength': 8}, 'description': {'type': 'string', 'maxLength': 256, 'minLength': 16}, 'image': {'type': 'string'}, 'end_time': DefinitionsDatetime, 'start_time': DefinitionsDatetime, 'remark': {'type': 'string'}}, 'required': ['title', 'description']}
DefinitionsUpdatequestion = {'properties': {'title': {'type': 'string'}, 'type': {'type': 'string', 'enum': ['single_choice', 'multiple_choice']}, 'options': {'type': 'array', 'items': DefinitionsOptionwithanswer}}}
DefinitionsTestingstatistics = {'properties': {'total_count': {'type': 'integer'}, 'max_score': {'type': 'integer'}, 'avg_score': {'type': 'integer'}, 'min_score': {'type': 'integer'}, 'distributions': {'type': 'array', 'items': DefinitionsDistribution}}}
DefinitionsCreatequestion = {'properties': {'title': {'type': 'string'}, 'type': {'type': 'string', 'enum': ['single_choice', 'multiple_choice']}, 'options': {'type': 'array', 'items': DefinitionsOptionwithanswer}}}

validators = {
    ('tests_id_questions', 'GET'): {'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('self_tests_test_id_questions_id', 'PUT'): {'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}, 'json': DefinitionsUpdatequestion},
    ('tests_handpick', 'GET'): {'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('self_testings', 'GET'): {'args': {'properties': {'limit': {'description': 'limit in query', 'default': 20, 'type': 'integer', 'format': 'int32', 'required': False}, 'offset': {'description': 'offset in query', 'default': 0, 'type': 'integer', 'format': 'int32', 'required': False}}, 'required': []}, 'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('qc_cos_config', 'GET'): {'args': {'properties': {'cos_path': {'description': 'cos path', 'type': 'string', 'required': False}}, 'required': []}, 'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('self_tests_id', 'GET'): {'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('self_tests_id', 'PUT'): {'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}, 'json': DefinitionsUpdatetest},
    ('self_tests_id', 'DELETE'): {'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('self_tests', 'GET'): {'args': {'properties': {'limit': {'description': 'limit in query', 'default': 20, 'type': 'integer', 'format': 'int32', 'required': False}, 'offset': {'description': 'offset in query', 'default': 0, 'type': 'integer', 'format': 'int32', 'required': False}, 'status': {'enum': ['draft', 'published', 'withdraw'], 'description': 'test status in query', 'type': 'string', 'required': False}}, 'required': []}, 'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('self_tests', 'POST'): {'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}, 'json': DefinitionsCreatetest},
    ('tests_id_statistics', 'GET'): {'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('tests_id', 'GET'): {'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('tests_id_answers', 'POST'): {'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}, 'json': DefinitionsAnswerquestion},
    ('self_tests_id_questions', 'GET'): {'args': {'properties': {'step': {'description': 'step in query', 'type': 'integer', 'format': 'int32', 'default': 0}}, 'required': []}, 'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('self_tests_id_questions', 'POST'): {'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}, 'json': DefinitionsCreatequestion},
}

filters = {
    ('tests_id_questions', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': DefinitionsQuestion}}},
    ('self_tests_test_id_questions_id', 'PUT'): {200: {'headers': None, 'schema': DefinitionsQuestion}},
    ('tests_handpick', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': DefinitionsTest}}},
    ('self_testings', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': DefinitionsTesting}}},
    ('qc_cos_config', 'GET'): {200: {'headers': None, 'schema': DefinitionsQcosconfig}},
    ('self_tests_id', 'GET'): {200: {'headers': None, 'schema': DefinitionsTestdetail}},
    ('self_tests_id', 'PUT'): {200: {'headers': None, 'schema': DefinitionsTest}},
    ('self_tests_id', 'DELETE'): {204: {'headers': None, 'schema': DefinitionsSuccess}},
    ('self_tests', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': DefinitionsTestdetail}}},
    ('self_tests', 'POST'): {201: {'headers': None, 'schema': DefinitionsTestdetail}},
    ('tests_id_statistics', 'GET'): {200: {'headers': None, 'schema': DefinitionsTestingstatistics}},
    ('tests_id', 'GET'): {200: {'headers': None, 'schema': DefinitionsTest}},
    ('tests_id_answers', 'POST'): {201: {'headers': None, 'schema': DefinitionsAnswersuccess}},
    ('self_tests_id_questions', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': DefinitionsQuestiondetail}}},
    ('self_tests_id_questions', 'POST'): {201: {'headers': None, 'schema': DefinitionsQuestiondetail}},
}

scopes = {
    ('tests_id_questions', 'GET'): ['open'],
    ('self_tests_test_id_questions_id', 'PUT'): ['open'],
    ('tests_handpick', 'GET'): ['open'],
    ('self_testings', 'GET'): ['open'],
    ('qc_cos_config', 'GET'): ['open'],
    ('self_tests_id', 'GET'): ['open'],
    ('self_tests_id', 'PUT'): ['open'],
    ('self_tests_id', 'DELETE'): ['open'],
    ('self_tests', 'GET'): ['open'],
    ('self_tests', 'POST'): ['open'],
    ('tests_id_statistics', 'GET'): ['open'],
    ('tests_id', 'GET'): ['open'],
    ('tests_id_answers', 'POST'): ['open'],
    ('self_tests_id_questions', 'GET'): ['open'],
    ('self_tests_id_questions', 'POST'): ['open'],
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

