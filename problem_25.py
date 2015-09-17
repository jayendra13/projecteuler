
i1 = 1
i2 = 1
f  = 0
i  = 2
while (f/10**1001)<=0:
	f = i1 + i2
	i1 = i2 
	i2 = f
	i += 1
	print i,len(str(f))
	
print i, len(str(f))