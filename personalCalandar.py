import re, pdb

# See if user input matches string in months list
def similarMonths(months:list[str], pickMonth) -> list[str]:
	for i in months:
		same = re.match(i, pickMonth)

		if same:
			return i

# See if year is a leap year
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

	# MONTHS
	months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]


	try:
		leapYr = int(pickYear) % 4 # leap year formula
		if len(pickYear) != 4:
			print("Invalid Input\n")
			main()
	except ValueError:
		print("Invalid Input\n")	
		main()

	pickMonth = input("\nEnter a month: ").upper()

	# DAYS
	days = {months[0]: 31, months[1]: 28, months[2]: 31, months[3]: 30, months[4]: 31, months[5]: 30, months[6]: 31, 
	months[7]: 31, months[8]: 30, months[9]: 31, months[10]: 30, months[11]: 31}

	if similarMonths(months, pickMonth) is None:
		print("Invalid input\n")
		main()
	else:
		timeFrame = similarMonths(months, pickMonth), pickYear
		print(timeFrame, f"Days: {dayData(days, timeFrame, leapYr)}")

main()
