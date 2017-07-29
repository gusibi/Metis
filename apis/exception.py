#! -*- coding: utf-8 -*-
from sanic.response import json
from sanic.exceptions import SanicException


error_codes = {
    'wxapp_not_registered': ('The wxapp not registered', '微信没有注册'),
    'invalid_wxapp_code': ('Invalid wxapp code', '无效的code'),
    'invalid_token': ('Invalid token', '无效的token'),
    'wxapp_already_registered': ('The weixin app already registered', '账号已被注册'),
}

def add_status_code(code):
    """
    Decorator used for adding exceptions to _sanic_exceptions.
    """
    def class_decorator(cls):
        cls.status_code = code
        return cls
    return class_decorator


class ApiException(SanicException):

    def __init__(self, code, message=None, text=None, status_code=None):
        super().__init__(message)
        self.error_code = code
        _message, _text = error_codes.get(code, (None, None))
        self.message = message or _message
        self.text = text or _text

        if status_code is not None:
            self.status_code = status_code
        self.headers = {
            'Content-Type': 'application/json',
        }


@add_status_code(404)
class NotFound(ApiException):
    pass


@add_status_code(400)
class BadRequest(ApiException):
    pass


@add_status_code(401)
class Unauthorized(ApiException):
    pass


@add_status_code(403)
class Forbidden(ApiException):
    pass


@add_status_code(500)
class ServerError(ApiException):
    pass