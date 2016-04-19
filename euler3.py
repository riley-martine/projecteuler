from __future__ import division
import math

def isprime(int):
	for i in range (2, int):
		if int % i == 0:
			return False
	return True

def findfactor():
	for i in range (2, int(math.sqrt(600851474143))):
		if 600851475143 % i == 0:
			if isprime(i):
				print i
		i -= 1
findfactor()
