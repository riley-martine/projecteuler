def ispalindrome(num):
		if str(num)[::-1] == str(num):
			return True
		return False
largest = 0

for i in range (100, 999):
	for n in range (100, 999):
		if ispalindrome(n * i) and (n * i) > largest:
			largest = (n * i)
print largest
