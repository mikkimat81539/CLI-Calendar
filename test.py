# THIS IS A TEST FILE TO SEE HOW TO LINK DAY TO CORRESPONDING WEEK

import datetime, re

x = datetime.datetime(2009, 1, 1)

wk = x.strftime("%a")
print(wk)

userInput = input("Enter a day: ").capitalize()

same = re.match(userInput, wk)

if same:
    print(wk, "It is a match")
