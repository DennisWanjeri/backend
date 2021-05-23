#!/usr/bin/env python3

from flask import request
from typing import List, TypeVar
import os

class Auth:
    """authentification class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """validates whether authentication is required"""
        if not path or not excluded_paths:
            return True
        path = path + '/' if path[-1] != '/' else path
        has_wildcard = any(x.endswith("*") for x in excluded_paths)
        if not has_wildcard:
            return path not in excluded_paths
        for e in excluded_paths:
            if e.endswith("*"):
                if path.startswith(e[:1]):
                    return False
            if path == e:
                return False
        return True


    def authorization_header(self, request=None) -> str:
        """validates all requests to secure API"""
        if request is None:
            return None
        if request.headers.get('Authorization'):
            return request.headers.get('Authorization')
        else:
            return None

        
    def current_user(self, request=None) -> TypeVar('User'):
        return None

    def session_cookie(self, request=None):
        """returns a cookie value from request"""
        if request is None:
            return None
        cookie_name = os.getenv('SESSION_NAME')
        return request.cookies.get(cookie_name)
