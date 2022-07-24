#20/6/22 - KLB
#Recipe Cost Calculator
#String Analyser V1
#Aim - To attempt to create a basic version of my string analyser without it being in a function


#************** Main Routine ****************

import re

#works out whether string has numbers and seperates string into amount and item

test_strings = [
  "50kg",
  "1kg",
  "2 kilograms",
  "20 grams",
]

for item in test_strings:
 number = 4
 valid = False
  
  #regular expression to find if item starts with a number
 number_regex = "^[1-9][0-9]"

 #if item has a number, seperate it into two (number and letters)
 if re.match(number_regex, item):
     amount = float(item[0:1])
     unit = item[1:]

# remove white space around unit
     unit = unit.strip()

#Output details
     print("Amount:", amount)
     print("Unit:", unit) 
     print("Length of Unit:", len(unit))
     




   