# -*- coding: utf-8 -*-
from __future__ import absolute_import

from sanic import Blueprint

from .routes import routes
from .validators import security


@security.scopes_loader
def current_scopes():
    return ['register', 'open', 'login']

bp = Blueprint('auth', url_prefix='/auth')  # 需要加 url_prefix

for route in routes:
    route.pop('endpoint', None)
    bp.add_route(route.pop('resource'), *route.pop('urls'), **route)