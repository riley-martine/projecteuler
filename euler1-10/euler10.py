import math
total = 5

def isprime(num):
        for i in range (2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                        return False
        return True

for i in range (4, 2000000):
	if isprime(i):
		total += i

print total
