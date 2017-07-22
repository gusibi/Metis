# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.oauth_token import OauthToken
from .api.oauth_token_refresh import OauthTokenRefresh
from .api.oauth_token_info import OauthTokenInfo
from .api.oauth_bind import OauthBind
from .api.accounts_wxapp import AccountsWxapp
from .api.self_password import SelfPassword
from .api.self_password_reset import SelfPasswordReset


routes = [
    dict(resource=OauthToken.as_view(), urls=['/oauth/token'], endpoint='oauth_token'),
    dict(resource=OauthTokenRefresh.as_view(), urls=['/oauth/token/refresh'], endpoint='oauth_token_refresh'),
    dict(resource=OauthTokenInfo.as_view(), urls=['/oauth/token/info'], endpoint='oauth_token_info'),
    dict(resource=OauthBind.as_view(), urls=['/oauth/bind'], endpoint='oauth_bind'),
    dict(resource=AccountsWxapp.as_view(), urls=['/accounts/wxapp'], endpoint='accounts_wxapp'),
    dict(resource=SelfPassword.as_view(), urls=['/self/password'], endpoint='self_password'),
    dict(resource=SelfPasswordReset.as_view(), urls=['/self/password/reset'], endpoint='self_password_reset'),
]