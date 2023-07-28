#!/usr/bin/env python3

"""function called is_prime that takes a number as input and returns True if the number is prime, and False otherwise."""

def is_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2,n):
            if n % i == 0:
                return False
        return True
    
