import math
primecount = 0
testing = 1
def isprime(num):
	for i in range (2, int(math.sqrt(num)) + 1):
		if num % i == 0:
			return False
	return True

while 1 == 1:
	if isprime(testing):
		if primecount == 10001:
			break
		primecount += 1
	testing += 1
print testing
