import re, string

def similarMonths(months:list[str], pickMonth) -> list[str]:
	for i in months:
		same = re.match(i, pickMonth)

		if same:
			return i


def main():
	# USER INPUT
	pickYear = input("Enter a year: ")

	# LEAP YEAR FORMULA
	leapYr = int(pickYear) % 4

	# DAYS
	leapDays = 366
	regDays = 365

	# MONTHS
	months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

	if len(pickYear) != 4:
		print("Invalid Input\n")
		main()			

	pickMonth = input("\nEnter a month: ").upper()

	print(similarMonths(months, pickMonth), pickYear)

main()
