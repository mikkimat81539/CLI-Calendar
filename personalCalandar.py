import re

# See if user input matches string in months list
def similarMonths(months:list[str], pickMonth) -> list[str]:
	for i in months:
		same = re.match(i, pickMonth)

		if same:
			return i
def dayData():
	pass

def main():
	# USER INPUT
	pickYear = input("Enter a year: ")

	# LEAP YEAR FORMULA
	leapYr = int(pickYear) % 4

	# MONTHS
	months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
	
	days = {months[0]: 31, months[1]: 28, months[2]: 31, months[3]: 30}

	if len(pickYear) != 4:
		print("Invalid Input\n")
		main()			

	pickMonth = input("\nEnter a month: ").upper()

	if similarMonths(months, pickMonth) is None:
		print("Invalid input\n")
		main()
	else:

		print(similarMonths(months, pickMonth), pickYear)

	if similarMonths(months, pickMonth) == "FEB" and leapYr == 0:
		days[months[1]] = 29
		print(days[months[1]])
	else:
		print(days[months[1]])

main()
