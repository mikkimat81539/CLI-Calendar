import re, pdb, string

# See if user input matches string in months list
def similarMonths(months:list[str], pickMonth) -> list[str]:
	for i in months:
		same = re.match(i, pickMonth)

		if same:
			return i

# See if year is a leap year
def dayData(days:dict[str,int], timeFrame, leapYr) -> dict[str,int]:
	for key, value in days.items():
		if timeFrame[0] == "FEB" and leapYr == 0:
			value = 29
			return value

		elif timeFrame[0] == key:
			return value

def incrementDays(dayDisplay):
	#count = 0

	numStore = []
	dayList = []
	weekList = []

	for i in range(1, 42):
		#count += 1
		#formula = count % (dayDisplay + 1)

		if len(dayList) == 7:
			numStore.append(dayList)
			dayList = []

		if i > dayDisplay:
			i = ""

		dayList.append(i)

	# WEEKS
	for i in range(0, len(numStore)):
		weeks = {"MON": numStore[i][0], "TUE": numStore[i][1],
		"WED": numStore[i][2], "THU": numStore[i][3], 
		"FRI": numStore[i][4], "SAT": numStore[i][5], "SUN": numStore[i][6]}

		weekList.append(weeks)


	return weekList, dayList


def main():
	# USER INPUT
	pickYear = input("Enter a year: ")

	# MONTHS
	months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

	try:	
		leapYr = int(pickYear) % 4 # leap year formula

	except ValueError:
		print("Invalid Input\n")
		return

	try:
		if len(pickYear) != 4:
			print("Invalid Input\n")
			return

		for i in pickYear:
			if i in string.ascii_letters:
				print("Invalid Input\n")
				return

	except ValueError:
		print("Invalid Input\n")	
		main()

	pickMonth = input("\nEnter a month: ").upper()

	# DAYS -- has max days with corresponding month
	days = {months[0]: 31, months[1]: 28, months[2]: 31, months[3]: 30, months[4]: 31, months[5]: 30, months[6]: 31, 
	months[7]: 31, months[8]: 30, months[9]: 31, months[10]: 30, months[11]: 31}


	if similarMonths(months, pickMonth) is None:
		print("Invalid input\n")
		main()
	else:
		timeFrame = similarMonths(months, pickMonth), pickYear
		dayDisplay = dayData(days, timeFrame, leapYr)

		weekDisplay = incrementDays(dayDisplay)

		print(timeFrame, f"Day: {weekDisplay}")

main()
