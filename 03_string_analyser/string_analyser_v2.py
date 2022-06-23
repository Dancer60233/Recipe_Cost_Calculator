#20/6/22 - KLB
#Recipe Cost Calculator
#String Analyser V2
#Aim - To attempt to create a basic version of my string analyser without it being in a function


#************** Main Routine ****************

import re

#works out whether string has numbers and seperates string into amount and item

test_strings = [
  "500kg",
  "1kg",
  "2 kilograms",
  "20 grams",
]

for item in test_strings:
  #regular expression to find if item starts with a number
 number_regex = "^[1-9][0-9][0-9]"

 #if item has a number, seperate it into two (number and letters)
 if re.match(number_regex, item):
     amount = item[0:2]
     unit = item[2:]

# remove white space around snack
     unit = unit.strip()
     print("Amount:", amount)
     print("Unit:", unit) 
     print("Length of Unit:", len(unit))
     


#print order
 


   