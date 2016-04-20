'''
A Decent Number has the following properties:

Its digits can only be 3's and/or 5's.
The number of 3's it contains is divisible by 5.
The number of 5's it contains is divisible by 3.
If there are more than one such number, we pick the largest one.
'''
def sherlock_beast():
	t = int(input().strip())
	for a0 in range(t):
		n = int(input().strip())
		temp = n
		while n%3 != 0:
			n -= 5
			pass
		if n < 0:
			print(-1)
		else:
			print('5' * n + '3' * (temp-n))

	


	