import re

def main():
	# USER INPUT
	pickMonth = input("Enter a month: ")

	pickYear = input("Enter a year: ")

	# LEAP YEAR FORMULA
	leapYr = int(pickYear) % 4

	if len(pickYear) != 4:
		main()			

	else:
		print(pickMonth, pickYear)

main()
