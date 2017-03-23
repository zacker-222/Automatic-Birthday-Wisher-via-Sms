from datetime import datetime
from msg import msg
fi=open("bdayinfo.txt","r")
import time

def done():
	l=[]
	w=open('dont.txt','r')
	while True:
		line=w.readline().strip()
		if line=='':
			break

		l.append(line.split(','))
	return l
li=[]
while True:
	d=fi.readline().strip()
	if d=='':
		break
	li.append(d)

while True:
	today=str(datetime.today()).split()[0]
	cur_year,cur_mon,cur_date=today.split('-')
	for data in li:

		date,month,name,number=data.split(',')
		List=done()	
		if date==cur_date and month==cur_mon:
			if [cur_year,cur_mon,cur_date,name] not in List:
				
				if str(number) =='9409213105':
					print 'het'
					time.sleep(5)
				print  msg('9409213105','asdfgh','Happy Birthday',str(number))
				
				time.sleep(10)
				with open("dont.txt","a+") as wr:
					wr.write(cur_year+","+cur_mon+","+cur_date+","+name)
				
			