import re, pdb, string

#This function is here so that it can take the list of months in the main function and the user input (pickMonth) and output the selected month from the list
def similarMonths(months:list[str], pickMonth) -> list[str]:
	for i in months:
		same = re.match(i, pickMonth) # This is here just in case the user types whole month

		# The program needs to return what closely matches the user input
		if same:
			return i

# This function is here to determine whether the year is a leap year and to display the number of days in the selected month
def dayData(days:dict[str,int], timeFrame, leapYr) -> dict[str,int]:
	for key, value in days.items():
		if timeFrame[0] == "FEB" and leapYr == 0: # If the user inputs feb and a leap year than output 29 days
			value = 29
			return value

		elif timeFrame[0] == key: # If not a leap year than output standard days
			return value

# This function is created to increment the days and output the days with the weekday
def incrementDays(dayDisplay):
	#count = 0

	numStore = []
	dayList = []
	weekList = []

	for i in range(1, 42):
		#count += 1
		#formula = count % (dayDisplay + 1)

		if len(dayList) == 7: # Once the dayList has a length of 7, store data in numStore list and make dayList empty
			numStore.append(dayList)
			dayList = []

		if i > dayDisplay: # if i is greated than 29, 30 or 31 than replace with empty string
			i = ""

		dayList.append(i)

	# WEEKS
	for i in range(0, len(numStore)): # Add numbers from numStore list and import them to weeks
		weeks = {"MON": numStore[i][0], "TUE": numStore[i][1],
		"WED": numStore[i][2], "THU": numStore[i][3], 
		"FRI": numStore[i][4], "SAT": numStore[i][5], "SUN": numStore[i][6]}

		weekList.append(weeks) # add the dictionary into weeksList


	return weekList, dayList


def main():
	# USER INPUT
	pickYear = input("Enter a year: ")

	# MONTHS
	months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]


	try:
		leapYr = int(pickYear) % 4 # leap year formula


		if len(pickYear) != 4: # if user does not enter 4 characters than invalid
			print("Invalid Input\n")
			return

		for i in pickYear: # if user enters letters than invalid input
			if i in string.ascii_letters:
				print("Invalid Input\n")
				return

	except ValueError:
		print("Invalid Input\n")	
		main()

	pickMonth = input("\nEnter a month: ").upper()

	# DAYS -- has max days with corresponding month (Ex: Jan has 31 days)
	days = {months[0]: 31, months[1]: 28, months[2]: 31, months[3]: 30, months[4]: 31, months[5]: 30, months[6]: 31, 
	months[7]: 31, months[8]: 30, months[9]: 31, months[10]: 30, months[11]: 31}


	if similarMonths(months, pickMonth) is None: # If user does enter a month that is mentioned in the list it will return None
		print("Invalid input\n")
		main()
	else:
		timeFrame = similarMonths(months, pickMonth), pickYear # Output month and year that the user inputted
		dayDisplay = dayData(days, timeFrame, leapYr) # Output the number of days associated with the selected month

		weekDisplay = incrementDays(dayDisplay) # output the weeks linked to the number of days being outputted

		print(timeFrame, f"Day: {weekDisplay}")

main()
