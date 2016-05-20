#!/usr/bin/env python
"""finds sum of all primes below 2 million."""


import math
TOTAL = 5


def isprime(num):
    """check for primality."""
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
        return True

for n in range(4, 2000000):
    if isprime(n):
        TOTAL += n

print TOTAL
