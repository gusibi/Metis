# -*- coding: utf-8 -*-

# TODO: datetime support

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###

base_path = '/v1'


DefinitionsAuthentications = {'description': '用户详细授权数据', 'properties': {'wxapp': {'type': 'string'}, 'mobile': {'type': 'string'}}}
DefinitionsDistribution = {'properties': {'value': {'type': 'string'}, 'count': {'type': 'integer', 'format': 'int32'}}}
DefinitionsQcosconfig = {'properties': {'sign': {'type': 'string'}}}
DefinitionsOption = {'required': ['option'], 'properties': {'option': {'type': 'string'}}}
DefinitionsSuccess = {'properties': {'ok': {'type': 'boolean'}}}
DefinitionsOptionwithanswer = {'required': ['option', 'is_checked'], 'properties': {'value': {'type': 'string'}, 'is_checked': {'type': 'boolean'}}}
DefinitionsDatetime = {'type': 'string', 'format': 'datetime'}
DefinitionsAccount = {'description': 'account 基本信息', 'required': ['id'], 'properties': {'id': {'type': 'string'}, 'nickname': {'type': 'string'}, 'avatar': {'type': 'string'}}}
DefinitionsNone = {'type': 'object'}
DefinitionsError = {'properties': {'error_code': {'type': 'integer', 'format': 'int32'}, 'message': {'type': 'string'}, 'text': {'type': 'string'}}}
DefinitionsUpdatetest = {'properties': {'image': {'type': 'string'}, 'title': {'type': 'string', 'minLength': 8, 'maxLength': 128}, 'description': {'type': 'string', 'minLength': 16, 'maxLength': 256}, 'start_time': DefinitionsDatetime, 'end_time': DefinitionsDatetime, 'status': {'type': 'string', 'enum': ['published', 'withdraw']}}}
DefinitionsCreatetest = {'required': ['title', 'description'], 'properties': {'image': {'type': 'string'}, 'title': {'type': 'string', 'minLength': 8, 'maxLength': 128}, 'description': {'type': 'string', 'minLength': 16, 'maxLength': 256}, 'start_time': DefinitionsDatetime, 'end_time': DefinitionsDatetime}}
DefinitionsQuestion = {'required': ['title', 'options'], 'properties': {'title': {'type': 'string'}, 'options': {'type': 'array', 'items': DefinitionsOption}}}
DefinitionsTestingstatistics = {'properties': {'total_count': {'type': 'integer'}, 'max_score': {'type': 'integer'}, 'min_score': {'type': 'integer'}, 'avg_score': {'type': 'integer'}, 'distributions': {'type': 'array', 'items': DefinitionsDistribution}}}
DefinitionsAccountdetail = {'description': 'account 信息', 'required': ['id'], 'properties': {'id': {'type': 'string'}, 'username': {'type': 'string'}, 'nickname': {'type': 'string'}, 'avatar': {'type': 'string'}, 'authentications': DefinitionsAuthentications, 'created_time': DefinitionsDatetime}}
DefinitionsCreatequestion = {'properties': {'title': {'type': 'string'}, 'type': {'type': 'string', 'enum': ['single_choice', 'multiple_choice']}, 'options': {'type': 'array', 'items': DefinitionsOptionwithanswer}}}
DefinitionsQuestiondetail = {'required': ['title', 'options'], 'properties': {'title': {'type': 'string'}, 'type': {'type': 'string', 'enum': ['single_choice', 'multiple_choice']}, 'index': {'type': 'integer', 'format': 'int32'}, 'options': {'type': 'array', 'items': DefinitionsOptionwithanswer}}}
DefinitionsTest = {'required': ['id', 'title', 'description'], 'properties': {'id': {'type': 'string'}, 'image': {'type': 'string'}, 'title': {'type': 'string'}, 'description': {'type': 'string'}, 'start_time': DefinitionsDatetime, 'end_time': DefinitionsDatetime, 'creator': DefinitionsAccount, 'created_time': DefinitionsDatetime}}
DefinitionsTestdetail = {'required': ['id', 'title', 'description'], 'properties': {'id': {'type': 'string'}, 'image': {'type': 'string'}, 'title': {'type': 'string'}, 'description': {'type': 'string'}, 'date_start': {'type': 'string'}, 'date_end': {'type': 'string'}, 'time_start': {'type': 'string'}, 'time_end': {'type': 'string'}, 'status': {'type': 'string'}, 'start_time': DefinitionsDatetime, 'end_time': DefinitionsDatetime, 'creator': DefinitionsAccount, 'created_time': DefinitionsDatetime}}
DefinitionsTesting = {'required': ['id', 'score', 'title', 'description'], 'properties': {'id': {'type': 'string'}, 'score': {'type': 'integer', 'format': 'int32'}, 'image': {'type': 'string'}, 'title': {'type': 'string'}, 'description': {'type': 'string'}, 'creator': DefinitionsAccount, 'created_time': DefinitionsDatetime}}
DefinitionsUpdatequestion = {'properties': {'title': {'type': 'string'}, 'type': {'type': 'string', 'enum': ['single_choice', 'multiple_choice']}, 'options': {'type': 'array', 'items': DefinitionsOptionwithanswer}}}

validators = {
    ('self_tests', 'GET'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}, 'args': {'required': [], 'properties': {'status': {'description': 'test status in query', 'type': 'string', 'required': False, 'enum': ['draft', 'published', 'withdraw']}, 'offset': {'description': 'offset in query', 'type': 'integer', 'format': 'int32', 'default': 0, 'required': False}, 'limit': {'description': 'limit in query', 'type': 'integer', 'format': 'int32', 'default': 20, 'required': False}}}},
    ('self_tests', 'POST'): {'json': DefinitionsCreatetest, 'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('self_tests_id', 'GET'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('self_tests_id', 'PUT'): {'json': DefinitionsUpdatetest, 'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('self_tests_id', 'DELETE'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('self_tests_id_questions', 'GET'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('self_tests_id_questions', 'POST'): {'json': DefinitionsCreatequestion, 'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('self_tests_test_id_questions_id', 'POST'): {'json': DefinitionsUpdatequestion, 'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('self_testings', 'GET'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}, 'args': {'required': [], 'properties': {'offset': {'description': 'offset in query', 'type': 'integer', 'format': 'int32', 'default': 0, 'required': False}, 'limit': {'description': 'limit in query', 'type': 'integer', 'format': 'int32', 'default': 20, 'required': False}}}},
    ('tests_id', 'GET'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('tests_id_questions', 'GET'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('tests_id_statistics', 'GET'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('qc_cos_config', 'GET'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}, 'args': {'required': [], 'properties': {'cos_path': {'description': 'cos path', 'type': 'string', 'required': False}}}},
}

filters = {
    ('self_tests', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': DefinitionsTestdetail}}},
    ('self_tests', 'POST'): {201: {'headers': None, 'schema': DefinitionsTestdetail}},
    ('self_tests_id', 'GET'): {200: {'headers': None, 'schema': DefinitionsTestdetail}},
    ('self_tests_id', 'PUT'): {200: {'headers': None, 'schema': DefinitionsTest}},
    ('self_tests_id', 'DELETE'): {204: {'headers': None, 'schema': DefinitionsSuccess}},
    ('self_tests_id_questions', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': DefinitionsQuestiondetail}}},
    ('self_tests_id_questions', 'POST'): {201: {'headers': None, 'schema': DefinitionsQuestiondetail}},
    ('self_tests_test_id_questions_id', 'POST'): {200: {'headers': None, 'schema': DefinitionsQuestion}},
    ('self_testings', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': DefinitionsTesting}}},
    ('tests_id', 'GET'): {200: {'headers': None, 'schema': DefinitionsTest}},
    ('tests_id_questions', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': DefinitionsQuestion}}},
    ('tests_id_statistics', 'GET'): {200: {'headers': None, 'schema': DefinitionsTestingstatistics}},
    ('qc_cos_config', 'GET'): {200: {'headers': None, 'schema': DefinitionsQcosconfig}},
}

scopes = {
    ('self_tests', 'GET'): ['open'],
    ('self_tests', 'POST'): ['open'],
    ('self_tests_id', 'GET'): ['open'],
    ('self_tests_id', 'PUT'): ['open'],
    ('self_tests_id', 'DELETE'): ['open'],
    ('self_tests_id_questions', 'GET'): ['open'],
    ('self_tests_id_questions', 'POST'): ['open'],
    ('self_tests_test_id_questions_id', 'POST'): ['open'],
    ('self_testings', 'GET'): ['open'],
    ('tests_id', 'GET'): ['open'],
    ('tests_id_questions', 'GET'): ['open'],
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
                                       field=key,
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

