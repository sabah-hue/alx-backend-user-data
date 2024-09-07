#!/usr/bin/env python3
"""Basic authentication module for the API.
"""
from .auth import Auth
import base64
import binascii
from typing import Tuple, TypeVar
from models.user import User


class BasicAuth(Auth):
    """Basic auth class
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """base64"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split("Basic ")[1].strip()

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ decode"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            res = base64.b64decode(
                base64_authorization_header,
                validate=True,
            )
            return res.decode('utf-8')
        except (binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str,
            ) -> Tuple[str, str]:
        """user credentials"""
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        try:
            email, password = decoded_base64_authorization_header.split(':', 1)
        except ValueError:
            return None, None
        return email, password

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """user object credentials"""
        if user_email is None:
            return None
        if user_pwd is None:
            return None
        try:
            users = User.search(attributes={'email': user_email})
        except Exception:
            return None
        if len(users) <= 0:
            return None
        if not users[0].is_valid_password(user_pwd):
            return None
        return users[0]
