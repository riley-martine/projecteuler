from __future__ import division
from math import floor

def ispalindrome(num):
		if len(num) % 2 == 0:
			for n in (0, int((len(num) / 2))):
				if num[n] != num[len(num) - n - 1]:
					return False
		elif len(num) % 2 == 0:
			return True

		for i in (0, int(((len(num) - 1) / 2))):
			print i
			if num[i] != num[len(num) - i - 1]:
				return False
		return True

print ispalindrome((raw_input("input: ")))
