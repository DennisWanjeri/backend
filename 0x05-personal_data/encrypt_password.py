#!/data/data/com.termux/files/usr/bin/env python3
"""password encryption"""

import bcrypt

def hash_password(password: str) -> bytes:
    """hashing"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def is_valid(hashed_password: bytes, password: str) -> bool:
    """validates a hashed password against itself"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
