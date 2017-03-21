def respond(n):
	f=406095498349873
	mod=100000000000000
	p=1
	for i in range(f):
		p*=i
		p%=mod
	return p	

			
