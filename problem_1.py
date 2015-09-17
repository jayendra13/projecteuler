# Problem 1: Multiples of 3 and 5
# 
# If we list all the natural numbers below 10 that are multiples
# of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
# Answer is 233168
from math import ceil
n = 1000
k1 = 3.0
k2 = 5.0
k3 = k1*k2
l1 = ceil(n / k1)
l2 = ceil(n / k2)
l3 = ceil(n / k3)

l = max(l1,l2)
i=1

# sum all multiples of k1
sum = 0
while i<l1:
	sum += (k1*i)
	#print k1*i
	i += 1

# sum all multiples of k2
i=1
while i<l2:
	sum += (k2*i)
	#print k2*i
	i += 1
	
# deduct all multiples of k1*k2
i=1
while i<l3:
	sum -= (k3*i)
	#print k3*i
	i += 1
	
print sum