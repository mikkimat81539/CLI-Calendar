# THIS IS A TEST FILE TO SEE HOW TO LINK DAY TO CORRESPONDING WEEK

import datetime, re

#x = datetime.datetime(2009, 1, 1)
#
#wk = x.strftime("%a")
#print(wk)
#
#userInput = input("Enter a day: ").capitalize()
#
#same = re.match(userInput, wk)
#
#if same:
#    print(wk, "It is a match")

weekList = []

#for i in range(1, 8):
#	x = datetime.datetime(2008, 6, i)
#	weekList.append(x.strftime("%a"))


#for i in range(1, 8):
#	x = datetime.datetime(2001, 2, i+1)
#
#	#weekList.append(int(x.strftime("%w")))
#	weekList.append(x.weekday())
#
#print(weekList)
#	
#week = {"Sun":weekList[0], "Mon":weekList[1], "Tue":weekList[2], "Wed":weekList[3],
#	"Thu":weekList[4], "Fri":weekList[5], "Sat":weekList[6]}
#
#print(week)
#

days = []
week_day = []

for i in range(1, 8):
	x = datetime.datetime(2001, 2, i)
	# wk = x.weekday()
	days.append(x.strftime("%d"))
    
    
for i in range(1, 8):
	x = datetime.datetime(2001, 2, i)
	week_day.append(x.strftime("%a"))

week = {week_day[0]:days[0], week_day[1]:days[1], week_day[2]:days[2],
week_day[3]:days[3], week_day[4]:days[4], week_day[5]:days[5], week_day[6]:days[6]}
print(week)
