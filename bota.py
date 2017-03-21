def respond(n):
	f=4060954988
	mod=100000000000000
	p=1
	for i in range(f):
		p*=i
		p%=mod
	return p	

			
