from datetime import datetime
from msg import msg
fi=open("bdayinfo.txt","r")

today=str(datetime.today()).split()[0]
cur_year,cur_mon,cur_date=today.split('-')
while True:
	data=fi.readline().strip()
	
	if data=="end":
		break
	date,month,name,number=data.split(',')

	if date==cur_date and month==cur_mon:
		print name
		msg("9409213105","asdfgh","Happy Birthday "+name+"\nYash Shah",number)
		wr=open("dont.txt","w+")
		wr.write(cur_year)
		wr.close()

fi.close()