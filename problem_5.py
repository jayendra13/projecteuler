
lst = []
p = 1
for i in xrange(2,11):
	if p%i != 0:
		for l in lst:
			if i%l == 0:
				i = i/l
		p *= i
		lst.append(i)