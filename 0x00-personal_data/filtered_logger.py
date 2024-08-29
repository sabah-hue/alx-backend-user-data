#!/usr/bin/env python3
""" module """


import re
from typing import List
import logging


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> List:
    """ returned log message obfuscated """
    pattern = '|'.join(f'{f}=.*?{separator}' for f in fields)
    return re.sub(pattern, lambda match:
                  f"{match.group(0).split('=')[0]}={redaction}{separator}",
                  message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self):
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        NotImplementedError
