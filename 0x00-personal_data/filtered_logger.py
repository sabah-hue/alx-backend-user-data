#!/usr/bin/env python3
""" module """
import re
from typing import List


def filter_datum(fields: List[str],
                 redaction: str, message: str,
                 separator: str) -> List:
    """ returned log message obfuscated """
    pattern = '|'.join(f'{f}=.*?{separator}' for f in fields)
    return re.sub(pattern,
                  lambda match:
                  f"{match.group(0).split('=')[0]}={redaction}{separator}",
                  message)
