#!/usr/bin/env python
"""finds first triangle number to have over five hundred divisors."""


def triangle(number):
    """get triangle # number."""
    sum = 0
    for i in range(0, number + 1):
        sum += i
    return sum


def numberofdivisors(num):
    """find number of divisors."""
    divs = 0
    for i in range(1, num + 1):
        if num % i == 0:
            divs += 1
    return divs

for COUNT in range(11768, 100000):
    divvs = numberofdivisors(triangle(COUNT))
    if divvs > 500:
        print triangle(COUNT)
        exit()
    print COUNT
    print divvs
print "err"
