#!/usr/bin/env python3
""" Encryption Module """
import bcrypt


def hash_password(password: str) -> bytes:
    """ Generates hashed password """
    encoded = password.encode()
    return bcrypt.hashpw(encoded, bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Validates password matches the hashed password """
    check = False
    encoded = password.encode()
    if bcrypt.checkpw(encoded, hashed_password):
        check = True
    return check
