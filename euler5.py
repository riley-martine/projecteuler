testing = 2


def divbyfirst20(int):
	for i in range (11, 20):
		if int % i != 0:
			return False
	return True

while 1 == 1:
	if divbyfirst20(testing):
		break
	testing += 2

print testing
