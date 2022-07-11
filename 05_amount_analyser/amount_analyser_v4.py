#9/7/22 - KLB
#Recipe Cost Calculator
#Amount Analyser V4
#Aim - To add my gram conversion function to the amount analyser so it also produces amount in grams
#Reflection - 


#Functions

def amount_analyser(ingredient):

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

   desired_amount = desired_amount.strip()
   desired_unit = desired_unit.strip()

  #Use string check to see if unit is valid
   unit = string_check(desired_unit, valid_units)


  #Check if Amount is valid
   if desired_amount == "":
     amount = "invalid choice"

   else:
    amount = float(desired_amount)
    if amount < 0:
     amount = "invalid choice"
     
  #Print out of error message if needed

      #Error message if unit and amount invalid
   if unit == "invalid choice" and amount == "invalid choice":
      print("Invalid Choice! Please enter a valid unit and amount")
     
   
       #Error message if unit invalid
   elif unit == "invalid choice":
      print("Invalid Choice! Please enter a valid unit")
    #Error message if  amount invalid
   elif amount == "invalid choice":
      print("Invalid Choice! Please enter a valid amount")

  #Convert amount into grams
   if unit == "g":
    gram_amount = amount
   elif unit == "kg":
    gram_amount = amount * 1000
   elif unit == "tsp":
    gram_amount = amount * 5.69
   elif unit == "tbsp":
    gram_amount = amount * 17.07 
   elif unit == "cups":
    if ingredient == "butter":
      gram_amount = amount * 250
    elif ingredient == "sugar":
      gram_amount = amount * 250
    elif ingredient == "flour":
      gram_amount = amount * 125
    elif ingredient == "oil":
     gram_amount = amount * 220
    elif ingredient == "water":
     gram_amount = amount * 236 
    else:
      gram_amount = amount * 250
     
  return amount, unit, gram_amount
 
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
all_gram_amounts = []

valid_units =[
  ["g", "grams", "gram" ],
  ["kg", "kilograms", "kilogram", "kilos", "kilo"],
  ["tbsp", "tablespoon", "tablespoons"],
  ["tsp", "teaspoon", "teaspoons"],
  ["cups", "cup"]
]

#Ask for 4 amounts (repeats 4 times for testing)
for item in range(1):

  
  ingredient_name = input("Ingredient: ").lower()

  #Ask and spilt amount and unit
  desired_amount, desired_unit, amount_in_g = amount_analyser(ingredient_name)
  all_amounts.append(desired_amount)
  all_units.append(desired_unit)
  all_gram_amounts.append(amount_in_g)
  print("\n")

print("\n")

#Print out unit and amount seprately
number = 0
for amount in all_amounts:
  
  print("Amount: {},   Unit: {}, Amount in Grams: {}".format(amount, all_units[number], all_gram_amounts[number]))
  number += 1
   