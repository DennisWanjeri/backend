#!/usr/bin/env python3
"""database module"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from user import Base, User


class DB:
    """class DB"""
    def __init__(self):
        """constructor"""
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """adds user to database"""
        new_user = User()
        new_user.email = email
        new_user.hashed_password = hashed_password

        session = self._session
        session.add(new_user)
        session.commit()

        return new_user
