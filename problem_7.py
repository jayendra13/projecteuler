
lst = []
p   = 1
n   = 10001
i   = 0

while i < n:

	p += 1
	is_prime = True
	for l in lst:
		if p%l == 0:
			is_prime = False
			break
	
	if is_prime:
		lst.append(p)
		print p
		i += 1
		
#print p