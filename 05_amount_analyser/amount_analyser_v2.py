#6/7/22 - KLB
#Recipe Cost Calculator
#Amount Analyser V2
#Aim - To add my intchecker to the code so I have error prevention for the amount
#Reflection - Code has error prevention however the it provides two error messages if both the unit and amount are wrong. My goal is to chage that in the next version.


#Functions

def amount_analyser():

  unit = "invalid choice"
  amount = "invalid choice"
  
  
  while unit == "invalid choice" or amount == "invalid choice":
   desired_amount = ""
   desired_unit = ""

  #Ask user for ingredient amount
   ingredient_amount = input("Ingredient Amount: ")

  #Seperate amount and unit
   for m in ingredient_amount:
     
    if m.isdigit() or m == "." or m == "-":
        desired_amount = desired_amount + m
        
    else:
      desired_unit = desired_unit + m

  
   desired_unit = desired_unit.strip()

  #Use string check to see if unit is valid
   unit = string_check(desired_unit, valid_units)
   if unit == "invalid choice":
     print("Invalid Choice! Please enter a valid unit")

  #Check if Amount is valid
   if desired_amount == "":
     print("Please enter an amount!")

   else:
    amount = float(desired_amount)
    if amount > 0:
     continue
    else:
     amount = "invalid choice"
     print("Invalid Choice! Please enter a valid amount")
     
  return amount, unit
 
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

print("\n")

#Print out unit and amount seprately
number = 0
for amount in all_amounts:
  
  print("Amount: {},   Unit: {}".format(amount, all_units[number]))
  number += 1
   