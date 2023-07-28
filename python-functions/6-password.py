#!/usr/bin/env python3


def validate_password(password):
    if len(password) < 8:
        return False
    elif password.find(" ") != -1:
        return False
    elif password.islower():
        return False
    elif password.isupper():
        return False
    else:
        return True
    
print(validate_password("Password123"))
print(validate_password("abc123"))
print(validate_password("Password 123"))
print(validate_password("password123"))
    