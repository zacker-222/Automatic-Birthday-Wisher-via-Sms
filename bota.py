def respond(n):
	f=406000000
	mod=1000000000
	p=1
	for i in range(f):
		p*=i
		p%=mod
	return p	

			
