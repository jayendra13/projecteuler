# Problem 3: Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

from math import floor, sqrt

n = 600851475143
sqrt_n = floor(sqrt(n))

primes = []
#prime_factors = []
i=1
while i <= sqrt_n:

	i += 1
	is_prime = 1
	for p in primes:
		if i%p == 0:
			is_prime = 0
			break
	
	if is_prime:
		#print i
		primes.append(i)
		if n%i == 0:
			print '%d is divisble by %d'%(n,i)
			#prime_factors.append(i)
			n = n/i
			sqrt_n = floor(sqrt(n))
print n