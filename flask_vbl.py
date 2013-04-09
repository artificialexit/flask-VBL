import requests
import json

from flask import request, current_app, redirect, _request_ctx_stack, session
from werkzeug.local import LocalProxy
from urlparse import urlunparse
from urllib import urlencode
from functools import wraps
from pprint import pformat

class VBL(object):
    cookie_key = 'vbl_PHPSESSID'
    url_base = 'vbl.synchrotron.org.au'
    epn_list = 'MXAutorickshaw/epn_list.php'
    session_key = 'vbl_auth'
    
    def __init__(self, app=None):
        if app is not None:
            self.app = app
            self.init_app(self.app)
        else:
            self.app = None
    

    def init_app(self, app):
        app.vbl = self
        
        app.before_request(self._load_user)
    
    def _load_user(self):
        ctx = _request_ctx_stack.top
        if self.session_key in session:
            ctx.user = session.get(self.session_key)
        elif self.cookie_key in request.cookies:
            ctx.user = self._get_session()
        else:
            ctx.user = None
        
    def _get_vbl_url(self, path, params=''):
        return urlunparse((request.scheme, self.url_base, path, '', params, ''))    
    
    def get_login_redirect(self):        
        params = urlencode({'redirect': request.url})
        url = self._get_vbl_url('index.php', params)
        return redirect(url)
 
    def _get_session(self):
        r = requests.get(self._get_vbl_url(self.epn_list),
                         cookies={self.cookie_key:request.cookies.get(self.cookie_key)})
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError:
            return
        session[self.session_key] = json.loads(r.text)
        return session[self.session_key]

    def requires_auth(self, f):
        @wraps(f)
        def decorated(*args, **kwargs):
            if not self.current_user:
                return self.get_login_redirect()
            return f(*args, **kwargs)
        return decorated

    @property    
    def current_user(self):
        return _request_ctx_stack.top.user
    