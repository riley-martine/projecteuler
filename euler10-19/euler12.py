#!/usr/bin/env python
"""finds first triangle number to have over five hundred divisors."""

import math


def triangle(number):
    """get triangle # number."""
    return (number * (number + 1)) / 2


def numberofdivisors(num):
    """find number of divisors."""
    divs = 0
    for i in xrange(1, int(math.ceil(math.sqrt(num)))):
        if num % i == 0:
            divs += 2
        if i*i == num:
            divs -= 1
    return divs

for COUNT in range(2, 100000):
    divvs = numberofdivisors(triangle(COUNT))
    if divvs > 500:
        print triangle(COUNT)
        exit()
    print COUNT
    print divvs
print "err"
