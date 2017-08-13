# -*- coding: utf-8 -*-
from __future__ import absolute_import

from sanic import Blueprint

from apis.verification import verify_request, current_account

from .routes import routes
from .validators import security


@security.scopes_loader
def current_scopes(request):
    is_validate, token = verify_request(request)
    if is_validate and token:
        if isinstance(token, list):
            return token
        current_account.id = token.sub
        return token.scopes
    return []

bp = Blueprint('auth', url_prefix='/auth')  # 需要加 url_prefix

for route in routes:
    route.pop('endpoint', None)
    bp.add_route(route.pop('resource'), *route.pop('urls'), **route)
