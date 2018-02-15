# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.oauth_token_code import OauthTokenCode
from .api.accounts_self import AccountsSelf
from .api.oauth_token import OauthToken
from .api.self_password_reset import SelfPasswordReset
from .api.self_password import SelfPassword
from .api.oauth_token_refresh import OauthTokenRefresh
from .api.accounts_wxapp import AccountsWxapp


routes = [
    dict(resource=OauthTokenCode.as_view(), urls=['/oauth/token/code'], endpoint='oauth_token_code'),
    dict(resource=AccountsSelf.as_view(), urls=['/accounts/self'], endpoint='accounts_self'),
    dict(resource=OauthToken.as_view(), urls=['/oauth/token'], endpoint='oauth_token'),
    dict(resource=SelfPasswordReset.as_view(), urls=['/self/password/reset'], endpoint='self_password_reset'),
    dict(resource=SelfPassword.as_view(), urls=['/self/password'], endpoint='self_password'),
    dict(resource=OauthTokenRefresh.as_view(), urls=['/oauth/token/refresh'], endpoint='oauth_token_refresh'),
    dict(resource=AccountsWxapp.as_view(), urls=['/accounts/wxapp'], endpoint='accounts_wxapp'),
]