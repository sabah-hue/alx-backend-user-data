#!/usr/bin/env python3
"""Auth module
"""
from flask import request
from typing import List, TypeVar
import fnmatch


class Auth:
    """Auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ check auth is required
        """
        if path is None:
            return True

        if excluded_paths is None or not excluded_paths:
            return True

        path = path.rstrip("/")
        for excluded_path in excluded_paths:
            # if fnmatch.fnmatch(path, excluded_path):
            #     return False
            if path == excluded_path.rstrip("/"):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ auth header
        """
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ get current user
        """
        return None
