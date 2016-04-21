import math
c = 0


for a in range (1, 1000):
	for b in range (1, 1000 - a):
		c = (1000 - a - b)
		if math.sqrt(a**2 + b**2) == c:
			print '-----'
			print a
			print b
			print c
			print '-----'
			print (a * b * c)
			break

