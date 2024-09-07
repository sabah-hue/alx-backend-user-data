#!/usr/bin/env python3
""" Module of Auth
"""
import request from flask


class Auth:
    """
    auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        require path
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        return flask object
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ return flask object """
        return None
