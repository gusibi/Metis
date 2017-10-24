# -*- coding: utf-8 -*-

# TODO: datetime support

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###

base_path = '/v1'


DefinitionsDistribution = {'properties': {'count': {'format': 'int32', 'type': 'integer'}, 'value': {'type': 'string'}}}
DefinitionsAuthentications = {'properties': {'wxapp': {'type': 'string'}, 'mobile': {'type': 'string'}}, 'description': '用户详细授权数据'}
DefinitionsNone = {'type': 'object'}
DefinitionsAnswerquestion = {'required': ['question_id', 'options'], 'properties': {'question_id': {'type': 'string'}, 'options': {'items': {'format': 'int32', 'type': 'integer'}, 'type': 'array'}}}
DefinitionsAccount = {'required': ['id'], 'properties': {'id': {'type': 'string'}, 'nickname': {'type': 'string'}, 'avatar': {'type': 'string'}}, 'description': 'account 基本信息'}
DefinitionsSuccess = {'properties': {'ok': {'type': 'boolean'}}}
DefinitionsAnswersuccess = {'properties': {'ok': {'type': 'boolean'}, 'last': {'type': 'boolean'}}}
DefinitionsDatetime = {'format': 'datetime', 'type': 'string'}
DefinitionsQcosconfig = {'properties': {'sign': {'type': 'string'}}}
DefinitionsOption = {'required': ['option'], 'properties': {'option': {'type': 'string'}, 'index': {'format': 'int32', 'type': 'integer'}}}
DefinitionsError = {'properties': {'error_code': {'format': 'int32', 'type': 'integer'}, 'text': {'type': 'string'}, 'message': {'type': 'string'}}}
DefinitionsOptionwithanswer = {'required': ['option', 'is_checked'], 'properties': {'option': {'type': 'string'}, 'is_checked': {'type': 'boolean'}, 'index': {'format': 'int32', 'type': 'integer'}}}
DefinitionsTestscore = {'properties': {'test_id': {'type': 'string'}, 'rank': {'type': 'integer'}, 'score': {'type': 'integer'}}}
DefinitionsTesting = {'required': ['id', 'score', 'title', 'description'], 'properties': {'creator': DefinitionsAccount, 'title': {'type': 'string'}, 'question_count': {'type': 'integer'}, 'score': {'format': 'int32', 'type': 'integer'}, 'description': {'type': 'string'}, 'image': {'type': 'string'}, 'created_time': DefinitionsDatetime, 'id': {'type': 'string'}}}
DefinitionsTestingstatistics = {'properties': {'total_count': {'type': 'integer'}, 'min_score': {'type': 'integer'}, 'max_score': {'type': 'integer'}, 'distributions': {'items': DefinitionsDistribution, 'type': 'array'}, 'avg_score': {'type': 'integer'}}}
DefinitionsTestdetail = {'required': ['id', 'title', 'description'], 'properties': {'date_end': {'type': 'string'}, 'creator': DefinitionsAccount, 'time_start': {'type': 'string'}, 'title': {'type': 'string'}, 'remark': {'type': 'string'}, 'status': {'type': 'string'}, 'question_count': {'type': 'integer'}, 'end_time': DefinitionsDatetime, 'id': {'type': 'string'}, 'time_end': {'type': 'string'}, 'start_time': DefinitionsDatetime, 'image': {'type': 'string'}, 'description': {'type': 'string'}, 'created_time': DefinitionsDatetime, 'date_start': {'type': 'string'}}}
DefinitionsCreatetest = {'required': ['title', 'description'], 'properties': {'title': {'minLength': 3, 'type': 'string', 'maxLength': 128}, 'remark': {'type': 'string'}, 'start_time': DefinitionsDatetime, 'image': {'type': 'string'}, 'description': {'minLength': 6, 'type': 'string', 'maxLength': 256}, 'end_time': DefinitionsDatetime}}
DefinitionsQuestion = {'required': ['id', 'title', 'options'], 'properties': {'options': {'items': DefinitionsOption, 'type': 'array'}, 'number': {'format': 'int32', 'type': 'integer'}, 'title': {'type': 'string'}, 'id': {'type': 'string'}}}
DefinitionsUpdatequestion = {'properties': {'options': {'items': DefinitionsOptionwithanswer, 'type': 'array'}, 'title': {'type': 'string'}, 'type': {'enum': ['single_choice', 'multiple_choice'], 'type': 'string'}}}
DefinitionsTest = {'required': ['id', 'title', 'description'], 'properties': {'creator': DefinitionsAccount, 'title': {'type': 'string'}, 'question_count': {'type': 'integer'}, 'end_time': DefinitionsDatetime, 'start_time': DefinitionsDatetime, 'image': {'type': 'string'}, 'description': {'type': 'string'}, 'created_time': DefinitionsDatetime, 'id': {'type': 'string'}}}
DefinitionsQuestiondetail = {'required': ['id', 'title', 'options'], 'properties': {'options': {'items': DefinitionsOptionwithanswer, 'type': 'array'}, 'id': {'type': 'string'}, 'number': {'format': 'int32', 'type': 'integer'}, 'title': {'type': 'string'}, 'type': {'enum': ['single_choice', 'multiple_choice'], 'type': 'string'}}}
DefinitionsAccountdetail = {'required': ['id'], 'properties': {'username': {'type': 'string'}, 'nickname': {'type': 'string'}, 'avatar': {'type': 'string'}, 'authentications': DefinitionsAuthentications, 'created_time': DefinitionsDatetime, 'id': {'type': 'string'}}, 'description': 'account 信息'}
DefinitionsCreatequestion = {'properties': {'options': {'items': DefinitionsOptionwithanswer, 'type': 'array'}, 'title': {'type': 'string'}, 'type': {'enum': ['single_choice', 'multiple_choice'], 'type': 'string'}}}
DefinitionsUpdatetest = {'properties': {'title': {'minLength': 3, 'type': 'string', 'maxLength': 128}, 'remark': {'type': 'string'}, 'start_time': DefinitionsDatetime, 'image': {'type': 'string'}, 'description': {'minLength': 6, 'type': 'string', 'maxLength': 256}, 'end_time': DefinitionsDatetime}}

validators = {
    ('tests_id', 'GET'): {'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('self_testings', 'GET'): {'args': {'properties': {'limit': {'default': 20, 'required': False, 'format': 'int32', 'description': 'limit in query', 'type': 'integer'}, 'offset': {'default': 0, 'required': False, 'format': 'int32', 'description': 'offset in query', 'type': 'integer'}}, 'required': []}, 'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('self_tests_id_publish', 'PUT'): {'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('self_tests_id_publish', 'DELETE'): {'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('tests_banner', 'GET'): {'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('tests_id_answers', 'POST'): {'json': DefinitionsAnswerquestion, 'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('self_tests', 'GET'): {'args': {'properties': {'status': {'enum': ['draft', 'published', 'withdraw'], 'required': False, 'description': 'test status in query', 'type': 'string'}, 'limit': {'default': 20, 'required': False, 'format': 'int32', 'description': 'limit in query', 'type': 'integer'}, 'offset': {'default': 0, 'required': False, 'format': 'int32', 'description': 'offset in query', 'type': 'integer'}}, 'required': []}, 'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('self_tests', 'POST'): {'json': DefinitionsCreatetest, 'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('tests_handpick', 'GET'): {'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('tests_id_score', 'GET'): {'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('self_tests_test_id_questions_id', 'PUT'): {'json': DefinitionsUpdatequestion, 'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('self_tests_id_questions', 'GET'): {'args': {'properties': {'step': {'default': 0, 'format': 'int32', 'description': 'step in query', 'type': 'integer'}}, 'required': []}, 'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('self_tests_id_questions', 'POST'): {'json': DefinitionsCreatequestion, 'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('tests_id_questions', 'GET'): {'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('tests_id_statistics', 'GET'): {'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('qc_cos_config', 'GET'): {'args': {'properties': {'cos_path': {'required': False, 'description': 'cos path', 'type': 'string'}}, 'required': []}, 'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('self_tests_id', 'GET'): {'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('self_tests_id', 'PUT'): {'json': DefinitionsUpdatetest, 'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
    ('self_tests_id', 'DELETE'): {'headers': {'properties': {'Authorization': {'type': 'string'}}, 'required': ['Authorization']}},
}

filters = {
    ('tests_id', 'GET'): {200: {'schema': DefinitionsTest, 'headers': None}},
    ('self_testings', 'GET'): {200: {'schema': {'items': DefinitionsTesting, 'type': 'array'}, 'headers': None}},
    ('self_tests_id_publish', 'PUT'): {200: {'schema': DefinitionsTestdetail, 'headers': None}},
    ('self_tests_id_publish', 'DELETE'): {204: {'schema': DefinitionsTestdetail, 'headers': None}},
    ('tests_banner', 'GET'): {200: {'schema': {'items': DefinitionsTest, 'type': 'array'}, 'headers': None}},
    ('tests_id_answers', 'POST'): {201: {'schema': DefinitionsAnswersuccess, 'headers': None}},
    ('self_tests', 'GET'): {200: {'schema': {'items': DefinitionsTestdetail, 'type': 'array'}, 'headers': None}},
    ('self_tests', 'POST'): {201: {'schema': DefinitionsTestdetail, 'headers': None}},
    ('tests_handpick', 'GET'): {200: {'schema': {'items': DefinitionsTest, 'type': 'array'}, 'headers': None}},
    ('tests_id_score', 'GET'): {200: {'schema': DefinitionsTestscore, 'headers': None}},
    ('self_tests_test_id_questions_id', 'PUT'): {200: {'schema': DefinitionsQuestion, 'headers': None}},
    ('self_tests_id_questions', 'GET'): {200: {'schema': {'items': DefinitionsQuestiondetail, 'type': 'array'}, 'headers': None}},
    ('self_tests_id_questions', 'POST'): {201: {'schema': DefinitionsQuestiondetail, 'headers': None}},
    ('tests_id_questions', 'GET'): {200: {'schema': {'items': DefinitionsQuestion, 'type': 'array'}, 'headers': None}},
    ('tests_id_statistics', 'GET'): {200: {'schema': DefinitionsTestingstatistics, 'headers': None}},
    ('qc_cos_config', 'GET'): {200: {'schema': DefinitionsQcosconfig, 'headers': None}},
    ('self_tests_id', 'GET'): {200: {'schema': DefinitionsTestdetail, 'headers': None}},
    ('self_tests_id', 'PUT'): {200: {'schema': DefinitionsTestdetail, 'headers': None}},
    ('self_tests_id', 'DELETE'): {204: {'schema': DefinitionsSuccess, 'headers': None}},
}

scopes = {
    ('tests_id', 'GET'): ['open'],
    ('self_testings', 'GET'): ['open'],
    ('self_tests_id_publish', 'PUT'): ['open'],
    ('self_tests_id_publish', 'DELETE'): ['open'],
    ('tests_banner', 'GET'): ['open'],
    ('tests_id_answers', 'POST'): ['open'],
    ('self_tests', 'GET'): ['open'],
    ('self_tests', 'POST'): ['open'],
    ('tests_handpick', 'GET'): ['open'],
    ('tests_id_score', 'GET'): ['open'],
    ('self_tests_test_id_questions_id', 'PUT'): ['open'],
    ('self_tests_id_questions', 'GET'): ['open'],
    ('self_tests_id_questions', 'POST'): ['open'],
    ('tests_id_questions', 'GET'): ['open'],
    ('tests_id_statistics', 'GET'): ['open'],
    ('qc_cos_config', 'GET'): ['open'],
    ('self_tests_id', 'GET'): ['open'],
    ('self_tests_id', 'PUT'): ['open'],
    ('self_tests_id', 'DELETE'): ['open'],
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

