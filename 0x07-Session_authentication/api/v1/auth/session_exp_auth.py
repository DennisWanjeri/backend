#!/usr/bin/env python3
"""session ID expiration module"""
import os
from api.v1.auth.session_auth import SessionAuth
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """session expiration"""

    def __init__(self):
        """constructor"""
        duration = os.getenv('SESSION_DURATION')
        if duration:
            try:
                self.session_duration = int(duration)
            except Exception:
                self.session_duration = 0
        else:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """creates a new session"""

        if user_id is not None:
            session_id = super().create_session(user_id)
            if not session_id:
                return None
            session_dict = {'user_id': user_id, 'created_at': datetime.now()}
            self.user_id_by_session_id[session_id] = session_dict
            return session_id

    def user_id_for_session_id(self, session_id=None):
        """user_id for session id"""
        if session_id is None:
            return None
        session_dict = self.user_id_by_session_id.get(session_id, None)
        if session_dict:
            user = session_dict.get('user_id', None)
            if user:
                sd = self.session_duration
                if sd <= 0:
                    return user
                created_at = session_dict.get('created_at', None)
                if not created_at:
                    return None
                if datetime.now() > created_at + timedelta(seconds=sd):
                    return Null
                return user
