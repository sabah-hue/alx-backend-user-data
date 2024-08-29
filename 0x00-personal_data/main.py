#!/usr/bin/env python3
import logging
import re
"""
Main file
"""

filter_datum = __import__('filtered_logger').filter_datum
RedactingFormatter = __import__('filtered_logger').RedactingFormatter

hash_password = __import__('encrypt_password').hash_password
is_valid = __import__('encrypt_password').is_valid


fields = ["password", "date_of_birth"]
messages = ["name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;", "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"]

for message in messages:
    print(filter_datum(fields, 'xxx', message, ';'))

message = "name=Bob;email=bob@dylan.com;ssn=000-123-0000;password=bobby2019;"
log_record = logging.LogRecord("my_logger", logging.INFO, None, None, message, None, None)
formatter = RedactingFormatter(fields=("email", "ssn", "password"))
print(formatter.format(log_record))

password = "MyAmazingPassw0rd"
print(hash_password(password))
print(hash_password(password))

password = "MyAmazingPassw0rd"
encrypted_password = hash_password(password)
print(encrypted_password)
print(is_valid(encrypted_password, password))
