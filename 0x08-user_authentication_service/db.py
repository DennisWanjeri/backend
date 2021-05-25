#!/usr/bin/env python3
"""database module"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from user import Base, User

VALID_FIELDS = ['id', 'email', 'hashed_password', 'session_id', 'reset_token']


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

    def find_user_by(self, **kwargs) -> User:
        """finds a user by abitrary keywords"""
        if not kwargs or any(x not in VALID_FIELDS for x in kwargs):
            raise InvalidRequestError
        session = self.__session
        try:
            return session.query(User).filter_by(**kwargs).one()
        except Exception:
            raise NoResultFound
        
        
    def update_user(self, user_id: int, **kwargs) -> None:
        """updates a user's attributes"""
        session = self.__session
        user = self.find_user_by(id=user_id)
        for k, v in kwargs.items():
            if k not in VALID_FIELDS:
                raise ValueError
            setattr(user, k, v)
        session.commit()
