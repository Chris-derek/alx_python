#!/usr/bin/env python3

"""function called validate_password that takes a password as input and performs the following checks.

The password must contain at least one uppercase letter.
The password must contain at least one lowercase letter.
The password should be at least 8 characters long.
The password should not contain spaces."""

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
    