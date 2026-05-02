import re, string

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

	for i in months:
		same = re.match(i, pickMonth)
		if same:
			print(i)
			break

	else:
		print(pickMonth, pickYear)

main()
