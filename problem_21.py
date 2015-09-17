# Amicable pairs under 10000 are
# 220 284
# 1184 1210
# 2620 2924
# 5020 5564
# 6232 6368
# and sum is 31626

from math import sqrt,ceil

def d(n):

	if n==1:
		return 1
	i=2
	sum = 1
	sqrt_n = ceil(sqrt(n))
	while i < sqrt_n:
		if n % i == 0:
			sum += i
			sum += (n/i)
		i += 1
	
	if sqrt_n**2 == n:
		sum += sqrt_n 
	return sum
	

lst = range(1,10001)
sum = 0
while lst:	
	y = d(lst[0])
	#print lst[0], y
	if y == 1:
		lst.remove(lst[0])
	else:
		x = d(y)
		if (x == lst[0]) & (x != y):
			sum += x
			sum += y
			print x, y
			lst.remove(x)
			lst.remove(y)
		else:
			lst.remove(lst[0])

print sum