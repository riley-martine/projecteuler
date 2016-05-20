#!/usr/bin/env python
"""finds largest palindrome made of products of 2 3 digit numbers"""


def ispalindrome(num):
    """checks if number is a palindrome"""
    if str(num)[::-1] == str(num):
        return True
    return False
LARGEST = 0

for i in range(100, 999):
    for n in range(100, 999):
        if ispalindrome(n * i) and (n * i) > LARGEST:
            LARGEST = (n * i)
print LARGEST
