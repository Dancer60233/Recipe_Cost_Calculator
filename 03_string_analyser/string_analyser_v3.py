#20/6/22 - KLB
#Recipe Cost Calculator
#String Analyser V3
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

amount = []
unit = []

for item in range(3):
 ing_amount = input("Ingredient Amount: ")
 for word in ing_amount.split():
   if word.isdigit():
      amount.append(int(word))
   else:
     unit.append(word)
     

print(amount)
print(unit)

     


#print order
 


   