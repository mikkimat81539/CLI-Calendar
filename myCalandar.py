# GOAL: MAKE A CALANDER IN THE CLI
# A calandar is a table that consist of years, months, weeks, days
# Since I am making a table i need to define columns (x) and rows (y)

# FIRST: MAKE A TABLE & ADD A TITLE -- DONE
# SECOND: ADD THE CURRENT YEAR -- DONE
	# Ask user to select year
# THIRD: ADD MONTH -- DONE
	# Ask user to select month

# FOURTH: ADD DAYS OF THE WEEK --DONE

# FIFTH: ADD DAYS
	# Days need to associate with week, month and year

import datetime, sys

try:
	yearPick = input("Enter a year: ").lower()

	wk = ["MON", "TUE", "WED", "THUR", "FRI", "SAT", "SUN"]

	if len(yearPick) != 4:
		print("Invalid Input")
		sys.exit()

	elif yearPick == "exit":
		sys.exit()	

	else:
		monthPick = int(input("Enter a month (1-12): "))

		if monthPick < 1 or monthPick > 12:
			print("Invalid Input")
			sys.exit()
		else:

			currentTime = datetime.datetime(int(yearPick), monthPick, 1)

			YEAR = currentTime.year
			MONTH = currentTime.strftime('%b')
			WEEK = currentTime.strftime('%w')

			# weekday() gives 0=Monday, 6=Sunday
			start_day = currentTime.weekday()

			if monthPick == 12:
				next_month = datetime.datetime(int(yearPick) + 1, 1, 1)
			else:
				next_month = datetime.datetime(int(yearPick), monthPick + 1, 1)
				days_in_month = (next_month - currentTime).days

			# Create a flat list of dates in order, filling empty spots with 0
			d = [0] * start_day  # empty spots before the first
			for day in range(1, days_in_month + 1):
				d.append(day)
			
			d_str = [f"{day:>2}" if day != 0 else "  " for day in d]
		
			title = "My CLI Calandar"

			print("Mo  Tu  We  Th  Fr  Sa  Su")
			print("_____________________________")

			for i in range(0, len(d_str), 7):
				row = d_str[i:i+7]
				# Fill missing cells if the last row has fewer than 7
				
				while len(row) < 7:
					row.append("  ")
				formatted_row = "".join(f" {cell}|" for cell in row)
				print(f"|{formatted_row}")
				print("|" + "___|"*7)

# 			table = f"""
# 							{title}
# 
# 				{MONTH} {YEAR}
# 
# 				
# 				{wk[0]} {wk[1]} {wk[2]} {wk[3]} {wk[4]} {wk[5]} {wk[6]}    
# 				_________________________________________________________
# 				|{d[0]} |{d[1]} |{d[2]}	|{d[3]} |{d[4]} |{d[5]}	|{d[6]} |
# 				|_______|_______|_______|_______|_______|_______|_______|
# 				|{d[7]}	|{d[8]} |{d[9]}	|{d[10]}|{d[11]}|{d[12]}|{d[13]}|
# 				|_______|_______|_______|_______|_______|_______|_______|
# 				|{d[14]}|{d[15]}|{d[16]}|{d[17]}|{d[18]}|{d[19]}|{d[20]}|
# 				|_______|_______|_______|_______|_______|_______|_______|
# 				|{d[21]}|{d[22]}|{d[23]}|{d[24]}|{d[25]}|{d[26]}|{d[27]}|
# 				|_______|_______|_______|_______|_______|_______|_______|	
# 				|{d[28]}|{d[29]}|{d[30]}|{d[31]}|{d[0]} |{d[1]} |{d[2]}	|
# 				|_______|_______|_______|_______|_______|_______|_______|	
# 				|{d[3]} |{d[4]} |{d[5]} |{d[6]} |{d[7]} |{d[8]} |{d[9]} |
# 				|_______|_______|_______|_______|_______|_______|_______|	
# 				|{d[10]}|{d[11]}|{d[12]}|{d[13]}|{d[14]}|{d[15]}|{d[16]}|
# 				|_______|_______|_______|_______|_______|_______|_______|
# 			"""
# 
# 			print(table)
# 
except ValueError:
	print("Invalid Input")
