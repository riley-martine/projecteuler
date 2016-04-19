from __future__ import division
fib1 = 0
fib2 = 1
total = 0
while fib1 < 4000000 and fib2 < 4000000:
	fib1 += fib2
	if (fib1 / 2) % 1 == 0:
		total += fib1
	fib2 += fib1
	if (fib2 / 2) % 1 == 0:
		total += fib2
print total
