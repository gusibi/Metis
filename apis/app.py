# -*- coding: utf-8 -*-

from sanic import Sanic
from sanic.response import json
from sanic.exceptions import NotFound as _NotFound, InvalidUsage
from apis.exception import (Unauthorized, NotFound, BadRequest,
                            Forbidden, RequestTimeout, ServerError)
from apis.custom_errors import (UnprocessableEntity,
                                ServerError as _ServerError,
                                Forbidden as _Forbidden)


from apis.settings import Config


def create_app(register_bp=True, test=False):
    app = Sanic(__name__)
    if test:
        app.config['TESTING'] = True
    app.config.from_object(Config)
    app.static('/static/', './apis/static')
    if register_bp:
       register_blueprints(app)
    return app


def register_blueprints(app):
    from apis.auth import bp as auth_bp
    from apis.v1 import bp as v1_bp
    app.blueprint(auth_bp)
    app.blueprint(v1_bp)


app = create_app()


all_json_errors = [BadRequest, Unauthorized, Forbidden,
                   NotFound, RequestTimeout, ServerError]


@app.exception(*all_json_errors)
def json_error(request, exception):
    return json(
        {
            'error_code': exception.error_code,
            'message': exception.message,
            'text': exception.text
        },
        status=exception.status_code)


# swagger validators 需要用到
@app.exception(_NotFound)
def not_found(request, exception):
    return json({'error_code': 'not_found',
                 'message': exception.args[0]},
                status=exception.status_code,
                )


@app.exception(UnprocessableEntity, _Forbidden, _ServerError)
def custom_json_errors(request, exception):
    return json(
        {
            'error_code': exception.error_code,
            'message': exception.message,
            'errors': exception.errors
        },
        status=exception.status_code)


@app.exception(InvalidUsage)
def method_not_allow(request, exception):
    return json({'error_code': 'method_not_allow',
                 'message': exception.args[0]},
                status=exception.status_code,
                )