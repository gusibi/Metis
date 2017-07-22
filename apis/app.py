# -*- coding: utf-8 -*-

from sanic import Sanic
from sanic.response import json
from sanic.exceptions import NotFound, InvalidUsage


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
    app.blueprint(auth_bp)


app = create_app()


@app.exception(NotFound)
def not_found(request, exception):
    print(exception)
    print(exception.args)
    return json({'error_code': 'not_found',
                 'message': exception.args[0]},
                status=exception.status_code,
                )


@app.exception(InvalidUsage)
def method_not_allow(request, exception):
    return json({'error_code': 'method_not_allow',
                 'message': exception.args[0]},
                status=exception.status_code,
                )
