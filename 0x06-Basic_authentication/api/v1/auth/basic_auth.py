#!/usr/bin/python3


import base64
from .auth import Auth
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """Basic Authentication"""
    def extract_base64_authorization_header(self, authorization_header: str) ->str:
        """returns Base64 part of the Authorization header for Basic Authentication"""
        if authorization_header is None or type(authorization_header) is not str:
            return None
        elif authorization_header.startswith("Basic ") is False:
            return None
    
        else:
            return authorization_header.split()[1]

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """returns decoded value of base64 string"""
        if base64_authorization_header is None or type(base64_authorization_header) is not str:
            return None
        try:
            is_true = base64.b64encode(base64.b64decode(base64_authorization_header)) == base64_authorization_header
            return base64.b64decode(base64_authorization_header).decode('utf-8')
        except Exception as e:
            return None
        
    def extract_user_credentials(self, decoded_base64_authorization_header:str) -> (str, str):
        """extracts user credentials from a decoded string"""
        if decoded_base64_authorization_header is None or type(decoded_base64_authorization_header) is not str:
            return (None, None)
        if ':'not in decoded_base64_authorization_header:
            return (None, None)
        
        decoded_b64 = decoded_base64_authorization_header.split(':', 1)
        return (decoded_b64[0], decoded_b64[1])
    
    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        if user_email is None or user_pwd is None or type(user_email) != str or type(user_pwd) != str:
            return None

        user = User().search({"email": user_email})
        if len(user) == 0 or user[0].is_valid_password(user_pwd) is False:
            return None
        else:
            return user[0]

    def current_user(self, request=None) -> TypeVar('User'):
        """overloads Auth and retreives the User instance for a request"""
        if request:
            header = self.authorization_header(request)
            base64_key = self.extract_base64_authorization_header(header)
            user_pwd = self.decode_base64_authorization_header(base64_key)
            user, pwd = self.extract_user_credentials(user_pwd)
            user = self.user_object_from_credentials(user, pwd)
            return user
