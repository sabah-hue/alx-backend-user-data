#!/usr/bin/env python3
"""Basic authentication module for the API.
"""
from .auth import Auth


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
