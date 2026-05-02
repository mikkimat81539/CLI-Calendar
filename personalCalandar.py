import re, pdb

# See if user input matches string in months list
def similarMonths(months:list[str], pickMonth) -> list[str]:
	for i in months:
		same = re.match(i, pickMonth)

		if same:
			return i
def dayData(days:dict[str,int], timeFrame, leapYr) -> dict[str,int]:
	for key, value in days.items():
		#breakpoint()	
		if timeFrame[0] == "FEB" and leapYr == 0:
			value = 29
			print(value)
			return value

		elif timeFrame[0] == key:
			return value

def main():
	# USER INPUT
	pickYear = input("Enter a year: ")

	# LEAP YEAR FORMULA
	#leapYr = int(pickYear) % 4

	# MONTHS
	months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

	#days = {months[0]: 31, months[1]: 28, months[2]: 31, months[3]: 30}

	try:
		leapYr = int(pickYear) % 4
		if len(pickYear) != 4:
			print("Invalid Input\n")
			main()
	except ValueError:
		print("Invalid Input\n")	
		main()

	pickMonth = input("\nEnter a month: ").upper()

	# DAYS
	days = {months[0]: 31, months[1]: 28, months[2]: 31, months[3]: 30}

	if similarMonths(months, pickMonth) is None:
		print("Invalid input\n")
		main()
	else:
		timeFrame = similarMonths(months, pickMonth), pickYear
		print(timeFrame, dayData(days, timeFrame, leapYr))


	#if timeFrame == "FEB" and leapYr == 0:
		#days[months[1]] = 29
		#print(days[months[1]])
	#else:
		#print(days[months[1]])

main()
