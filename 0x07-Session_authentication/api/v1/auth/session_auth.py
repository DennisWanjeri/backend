#!/usr/bin/end python3
"""session Authentication"""
from .auth import Auth
import base64
from models.user import User
from typing import TypeVar
import uuid


class SessionAuth(Auth):
    """session authentication class, inherits from Auth"""
    user_id_by_session_id = dict()

    def create_session(self, user_id: str = None) -> str:
        """creates a Session ID for a user_id"""
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id
    
    def user_id_for_session_id(self, session_id: str = None) -> str:
        """returns a user ID based on session ID"""
        if session_id is None or type(session_id) != str:
            return None
        value = self.user_id_by_session_id.get(session_id)
        return value

    def current_user(self, request=None) -> str:
        """return user based on cookie value"""
        if request == None:
            return None
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        if session_id is not None and user_id is not None:
            return User.get(user_id)
        return None

    def destroy_session(self, request=None):
        """deletes user session/logout"""
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return False

        del self.user_id_by_session_id[session_id]
        return True
