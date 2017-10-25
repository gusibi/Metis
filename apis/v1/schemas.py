# -*- coding: utf-8 -*-

# TODO: datetime support

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###

base_path = '/v1'


DefinitionsOption = {'properties': {'index': {'type': 'integer', 'format': 'int32'}, 'option': {'type': 'string'}}, 'required': ['option']}
DefinitionsDistribution = {'properties': {'value': {'type': 'string'}, 'count': {'type': 'integer', 'format': 'int32'}}}
DefinitionsTestscore = {'properties': {'score': {'type': 'integer'}, 'rank': {'type': 'integer'}, 'test_id': {'type': 'string'}}}
DefinitionsAuthentications = {'properties': {'wxapp': {'type': 'string'}, 'mobile': {'type': 'string'}}, 'description': '用户详细授权数据'}
DefinitionsSuccess = {'properties': {'ok': {'type': 'boolean'}}}
DefinitionsAnswerquestion = {'properties': {'question_id': {'type': 'string'}, 'options': {'type': 'array', 'items': {'type': 'integer', 'format': 'int32'}}}, 'required': ['question_id', 'options']}
DefinitionsOptionwithanswer = {'properties': {'is_checked': {'type': 'boolean'}, 'index': {'type': 'integer', 'format': 'int32'}, 'option': {'type': 'string'}}, 'required': ['option', 'is_checked']}
DefinitionsError = {'properties': {'message': {'type': 'string'}, 'text': {'type': 'string'}, 'error_code': {'type': 'integer', 'format': 'int32'}}}
DefinitionsNone = {'type': 'object'}
DefinitionsDatetime = {'type': 'string', 'format': 'datetime'}
DefinitionsAnswersuccess = {'properties': {'ok': {'type': 'boolean'}, 'last': {'type': 'boolean'}}}
DefinitionsQcosconfig = {'properties': {'sign': {'type': 'string'}}}
DefinitionsAccount = {'properties': {'nickname': {'type': 'string'}, 'avatar': {'type': 'string'}, 'id': {'type': 'string'}}, 'required': ['id'], 'description': 'account 基本信息'}
DefinitionsTest = {'properties': {'description': {'type': 'string'}, 'title': {'type': 'string'}, 'id': {'type': 'string'}, 'start_time': DefinitionsDatetime, 'end_time': DefinitionsDatetime, 'question_count': {'type': 'integer'}, 'created_time': DefinitionsDatetime, 'image': {'type': 'string'}, 'creator': DefinitionsAccount}, 'required': ['id', 'title', 'description']}
DefinitionsUpdatetest = {'properties': {'remark': {'type': 'string'}, 'end_time': DefinitionsDatetime, 'title': {'type': 'string', 'maxLength': 128, 'minLength': 3}, 'description': {'type': 'string', 'maxLength': 256, 'minLength': 6}, 'image': {'type': 'string'}, 'start_time': DefinitionsDatetime}}
DefinitionsCreatequestion = {'properties': {'type': {'type': 'string', 'enum': ['single_choice', 'multiple_choice']}, 'options': {'type': 'array', 'items': DefinitionsOptionwithanswer}, 'title': {'type': 'string'}}}
DefinitionsQuestiondetail = {'properties': {'number': {'type': 'integer', 'format': 'int32'}, 'type': {'type': 'string', 'enum': ['single_choice', 'multiple_choice']}, 'options': {'type': 'array', 'items': DefinitionsOptionwithanswer}, 'id': {'type': 'string'}, 'title': {'type': 'string'}}, 'required': ['id', 'title', 'options']}
DefinitionsCreatetest = {'properties': {'remark': {'type': 'string'}, 'end_time': DefinitionsDatetime, 'title': {'type': 'string', 'maxLength': 128, 'minLength': 3}, 'description': {'type': 'string', 'maxLength': 256, 'minLength': 6}, 'image': {'type': 'string'}, 'start_time': DefinitionsDatetime}, 'required': ['title', 'description']}
DefinitionsUpdatequestion = {'properties': {'type': {'type': 'string', 'enum': ['single_choice', 'multiple_choice']}, 'options': {'type': 'array', 'items': DefinitionsOptionwithanswer}, 'title': {'type': 'string'}}}
DefinitionsTestdetail = {'properties': {'time_start': {'type': 'string'}, 'date_start': {'type': 'string'}, 'image': {'type': 'string'}, 'date_end': {'type': 'string'}, 'status': {'type': 'string'}, 'id': {'type': 'string'}, 'time_end': {'type': 'string'}, 'description': {'type': 'string'}, 'remark': {'type': 'string'}, 'end_time': DefinitionsDatetime, 'title': {'type': 'string'}, 'created_time': DefinitionsDatetime, 'question_count': {'type': 'integer'}, 'start_time': DefinitionsDatetime, 'creator': DefinitionsAccount}, 'required': ['id', 'title', 'description']}
DefinitionsAccountdetail = {'properties': {'username': {'type': 'string'}, 'nickname': {'type': 'string'}, 'authentications': DefinitionsAuthentications, 'created_time': DefinitionsDatetime, 'avatar': {'type': 'string'}, 'id': {'type': 'string'}}, 'required': ['id'], 'description': 'account 信息'}
DefinitionsQuestion = {'properties': {'number': {'type': 'integer', 'format': 'int32'}, 'options': {'type': 'array', 'items': DefinitionsOption}, 'id': {'type': 'string'}, 'title': {'type': 'string'}}, 'required': ['id', 'title', 'options']}
DefinitionsTestingstatistics = {'properties': {'total_count': {'type': 'integer'}, 'distributions': {'type': 'array', 'items': DefinitionsDistribution}, 'max_score': {'type': 'integer'}, 'min_score': {'type': 'integer'}, 'avg_score': {'type': 'integer'}}}
DefinitionsTesting = {'properties': {'score': {'type': 'integer', 'format': 'int32'}, 'title': {'type': 'string'}, 'id': {'type': 'string'}, 'description': {'type': 'string'}, 'question_count': {'type': 'integer'}, 'created_time': DefinitionsDatetime, 'image': {'type': 'string'}, 'creator': DefinitionsAccount}, 'required': ['id', 'title', 'description']}

validators = {
    ('self_tests_test_id_questions_id', 'PUT'): {'json': DefinitionsUpdatequestion, 'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('self_testings', 'GET'): {'args': {'properties': {'offset': {'required': False, 'type': 'integer', 'description': 'offset in query', 'format': 'int32', 'default': 0}, 'limit': {'required': False, 'type': 'integer', 'description': 'limit in query', 'format': 'int32', 'default': 20}}, 'required': []}, 'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('self_tests_id', 'GET'): {'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('self_tests_id', 'DELETE'): {'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('self_tests_id', 'PUT'): {'json': DefinitionsUpdatetest, 'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('qc_cos_config', 'GET'): {'args': {'properties': {'cos_path': {'description': 'cos path', 'required': False, 'type': 'string'}}, 'required': []}, 'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('tests_id', 'GET'): {'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('tests_id_score', 'GET'): {'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('tests_id_statistics', 'GET'): {'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('tests_banner', 'GET'): {'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('self_tests_id_questions', 'GET'): {'args': {'properties': {'step': {'type': 'integer', 'default': 0, 'format': 'int32', 'description': 'step in query'}}, 'required': []}, 'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('self_tests_id_questions', 'POST'): {'json': DefinitionsCreatequestion, 'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('tests_id_answers', 'POST'): {'json': DefinitionsAnswerquestion, 'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('tests_handpick', 'GET'): {'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('self_tests', 'GET'): {'args': {'properties': {'offset': {'required': False, 'type': 'integer', 'description': 'offset in query', 'format': 'int32', 'default': 0}, 'limit': {'required': False, 'type': 'integer', 'description': 'limit in query', 'format': 'int32', 'default': 20}, 'status': {'enum': ['draft', 'published', 'withdraw'], 'required': False, 'type': 'string', 'description': 'test status in query'}}, 'required': []}, 'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('self_tests', 'POST'): {'json': DefinitionsCreatetest, 'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('tests_id_questions', 'GET'): {'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('self_tests_id_publish', 'PUT'): {'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('self_tests_id_publish', 'DELETE'): {'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
}

filters = {
    ('self_tests_test_id_questions_id', 'PUT'): {200: {'headers': None, 'schema': DefinitionsQuestion}},
    ('self_testings', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': DefinitionsTesting}}},
    ('self_tests_id', 'GET'): {200: {'headers': None, 'schema': DefinitionsTestdetail}},
    ('self_tests_id', 'DELETE'): {204: {'headers': None, 'schema': DefinitionsSuccess}},
    ('self_tests_id', 'PUT'): {200: {'headers': None, 'schema': DefinitionsTestdetail}},
    ('qc_cos_config', 'GET'): {200: {'headers': None, 'schema': DefinitionsQcosconfig}},
    ('tests_id', 'GET'): {200: {'headers': None, 'schema': DefinitionsTest}},
    ('tests_id_score', 'GET'): {200: {'headers': None, 'schema': DefinitionsTestscore}},
    ('tests_id_statistics', 'GET'): {200: {'headers': None, 'schema': DefinitionsTestingstatistics}},
    ('tests_banner', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': DefinitionsTest}}},
    ('self_tests_id_questions', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': DefinitionsQuestiondetail}}},
    ('self_tests_id_questions', 'POST'): {201: {'headers': None, 'schema': DefinitionsQuestiondetail}},
    ('tests_id_answers', 'POST'): {201: {'headers': None, 'schema': DefinitionsAnswersuccess}},
    ('tests_handpick', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': DefinitionsTest}}},
    ('self_tests', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': DefinitionsTestdetail}}},
    ('self_tests', 'POST'): {201: {'headers': None, 'schema': DefinitionsTestdetail}},
    ('tests_id_questions', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': DefinitionsQuestion}}},
    ('self_tests_id_publish', 'PUT'): {200: {'headers': None, 'schema': DefinitionsTestdetail}},
    ('self_tests_id_publish', 'DELETE'): {204: {'headers': None, 'schema': DefinitionsTestdetail}},
}

scopes = {
    ('self_tests_test_id_questions_id', 'PUT'): ['open'],
    ('self_testings', 'GET'): ['open'],
    ('self_tests_id', 'GET'): ['open'],
    ('self_tests_id', 'DELETE'): ['open'],
    ('self_tests_id', 'PUT'): ['open'],
    ('qc_cos_config', 'GET'): ['open'],
    ('tests_id', 'GET'): ['open'],
    ('tests_id_score', 'GET'): ['open'],
    ('tests_id_statistics', 'GET'): ['open'],
    ('tests_banner', 'GET'): ['open'],
    ('self_tests_id_questions', 'GET'): ['open'],
    ('self_tests_id_questions', 'POST'): ['open'],
    ('tests_id_answers', 'POST'): ['open'],
    ('tests_handpick', 'GET'): ['open'],
    ('self_tests', 'GET'): ['open'],
    ('self_tests', 'POST'): ['open'],
    ('tests_id_questions', 'GET'): ['open'],
    ('self_tests_id_publish', 'PUT'): ['open'],
    ('self_tests_id_publish', 'DELETE'): ['open'],
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

