from __future__ import division
total = 0
for i in range(0, 1000):
	if (i / 5) % 1 == 0:
                total += i
	elif (i / 3) % 1 == 0:
		total += i
print total
