#4/7/22 - KLB
#Recipe Cost Calculator
#Amount Analyser V1
#Aim - To create a basic version of my amount analyser that has error prevention for the unit and amount


def amount_analyser():
  desired_amount = ""
  desired_unit = ""
  unit = "invalid choice"
  amount = "invalid choice"
  
  while unit == "invalid choice":
   ingredient_amount = input("Ingredient Amount: ")
   for m in ingredient_amount:
    if m.isdigit() or m == ".":
        desired_amount = desired_amount + m
        
    else:
      desired_unit = desired_unit + m
      
   desired_unit = desired_unit.strip()
   desired_amount = desired_amount.strip
   unit = string_check(desired_unit, valid_units)
  return desired_amount, desired_unit
 
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

 if is_valid == "yes":
    return chosen

 else:
    return "invalid choice"
  



#Main Routine

all_amounts = []
all_units = []

valid_units =[
  ["g", "grams" ],
  ["kg", "kilograms"],
  ["tbsp", "tablespoon"],
  ["tsp", "teaspoon"]
]

#Ask for 4 amounts (repeats 4 times for testing)
for item in range(4):

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
   