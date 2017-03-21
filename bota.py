def respond(n):
	f=500000
	mod=1000000000
	p=1
	for i in range(1,f+1):
		p*=i
		p%=mod
	return p	

			
