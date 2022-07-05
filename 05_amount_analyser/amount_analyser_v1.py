#4/7/22 - KLB
#Recipe Cost Calculator
#Amount Analyser V1
#Aim - To create a basic version of my amount analyser that has error prevention for the unit


#Functions

def amount_analyser():

  unit = "invalid choice"
  
  
  while unit == "invalid choice":
   desired_amount = ""
   desired_unit = ""
    
   ingredient_amount = input("Ingredient Amount: ")
   for m in ingredient_amount:
    if m.isdigit() or m == ".":
        desired_amount = desired_amount + m
        
    else:
      desired_unit = desired_unit + m
      
   desired_unit = desired_unit.strip()
 
   unit = string_check(desired_unit, valid_units)
   if unit == "invalid choice":
     print("Invalid Choice! Please enter a valid unit")
  return desired_amount, unit
 
def string_check(choice, options):
 for var_list in options:
   #if snack is in one of the lists, return the full name
      if choice in var_list:
  #Get full name of snack and put it in titles case so it looks nice when outputted
       return var_list[0].lower()
       is_valid = "yes"
       break

      else:
        is_valid = "no"

 if is_valid == "no":
   return "invalid choice"
   
   
 else:
    return "invalid choice"
  



#Main Routine

all_amounts = []
all_units = []

valid_units =[
  ["g", "grams" ],
  ["kg", "kilograms", "kilogram", "kilos", "kilo"],
  ["tbsp", "tablespoon", "tablespoons"],
  ["tsp", "teaspoon", "teaspoon"]
]

#Ask for 4 amounts (repeats 4 times for testing)
for item in range(2):

  #Ask and spilt amount and unit
  desired_amount, desired_unit = amount_analyser()
  all_amounts.append(desired_amount)
  all_units.append(desired_unit)

print("\n")

#Print out unit and amount seprately
number = 0
for amount in all_amounts:
  
  print("Amount: {},   Unit: {}".format(amount, all_units[number]))
  number += 1
   