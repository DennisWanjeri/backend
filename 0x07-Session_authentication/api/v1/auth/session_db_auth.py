#!/usr/bin/env python3
"""database sessions"""
from api.v1.auth.session_exp_auth import SessionExpAuth
import os
from models.user_session import UserSession
from datetime import datetime, timedelta


class SessionDBAuth(SessionExpAuth):
    """Session Database Auth"""
    def create_session(self, user_id=None):
        """creates and stores a new instance of UserSession"""
        session_id = super().create_session(user_id)
        if not session_id:
            return None
        new_user = UserSession(user_id=user_id, session_id=session_id)
        new_user.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """returns user_id by requesting UserSession in database based on session_id"""
        if not session_id:
            return None
        try:
            user_list = UserSession.search({session_id: session_id})
            for user in user_list:
                created_at = user.get('created_at', None)
                if not created_at:
                    return None
                if (datetime.now() > created_at + timedelta(seconds=self.session_duration)):
                    return None
                return user.get('user_id', None)
        except Exception:
            return None

    def destroy_session(self, request=None) -> bool:
        """session termination"""
        if request:
            session_id = self.session_cookie(request)
            if session_id:
                if super().destroy_session(request):
                    try:
                        user_list = UserSession.search({session_id: session_id})
                        for user in user_list:
                            user.remove()
                            return True
                    except Exception:
                        return False
        return False
    
