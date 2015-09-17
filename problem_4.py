
lst = []
for i in xrange(999,90,-1):
	for j in xrange(999,90,-1):
		k = i*j
		p = str(k)
		mp = len(p)/2
		p1 = p[0:mp]
		if len(p)%2==0:
			p2 = p[mp:]
		else:
			p2 = p[mp+1:]
		p2 = p2[::-1]
		if p1 == p2:
			lst.append(k)
			
print max(lst)