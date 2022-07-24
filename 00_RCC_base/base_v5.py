#15/07/22 - KLB
#Recipe Cost Calculator
#Base V5
#Aim - To get my ingredient amount loop to properly function so there is also exit code

#------------Functions---------------

def not_blank(question):
  valid = False

  while not valid:
    response = input(question)

    if response != "":
      return response

    else:
      print("Sorry - This can't be blank")




def float_checker(question, type): 
  valid = False
  while not valid:

   #ask user for number and checks if it is valid
   try:
    response = float(input(question))

    if response > 0:
      valid = True
   #Checks if number is in range
    else:
     print("Invalid! Please enter a valid {}!".format(type))
   except:
     print("Invalid number! Please enter a valid number")

  return response
      

def string_check(choice, options):
 for var_list in options:
   #if unit is in one of the lists, return the full name
      if choice in var_list:
  #Get shorthand version of unit and return in lower case
       return var_list[0].lower()
       is_valid = "yes"
       break

      else:
        is_valid = "no"

 if is_valid == "no":
   return "invalid choice"
   
   
 else:
    return "invalid choice"
  










def amount_analyser(ingredient, question):

  unit = "invalid choice"
  amount = "invalid choice"
  
  
  while unit == "invalid choice" or amount == "invalid choice":
   desired_amount = ""
   desired_unit = ""

  #Ask user for ingredient amount
   ingredient_amount = input(question)

  #Seperate amount and unit
   for m in ingredient_amount:
     
    if m.isdigit() or m == "." or m == "-":
        desired_amount = desired_amount + m
        
    else:
      desired_unit = desired_unit + m

   desired_amount = desired_amount.strip()
   desired_unit = desired_unit.strip().lower()

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
   elif unit == "eggs":
    gram_amount = "egg"
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
 

def calc_ing_cost():
  print("calculate ingredient cost")

def calc_serving_cost():
 return "amount"

def space(num_spaces):
 for item in range (0, num_spaces):
   print()

  





#*************** Main Routine *************

#Temporary number of ingredients will ask user in future versions
num_ing = 3
all_amounts = []
all_units = []


valid_units =[
  ["g", "grams", "gram" ],
  ["kg", "kilograms", "kilogram", "kilos", "kilo"],
  ["tbsp", "tablespoon", "tablespoons"],
  ["tsp", "teaspoon", "teaspoons"],
  ["cups", "cup"],
  ["eggs", "egg"]
]

if __name__ == "__main__":

 #Welcome users
 print("Welcome to the Recipe Cost Calculator")

#Ask user for basic details about recipe
 recipe_name = not_blank("Recipe Name: ")
 serving_size = float_checker("Serving Size: ", "serving size")
 space(2)


ing_name = ""

#Loop until exit code is entered
while ing_name != "xxx":
   

   #Ingredient name 
   ing_name = not_blank("Ingredient Name: ").lower()

  #If exit code is entered stop loop
   if ing_name == "xxx":
     break

   
   #Ask for Amount of ingredient needed
   need_amount, need_unit, need_amount_in_g = amount_analyser(ing_name, "Ingredient Amount Needed: ")
   all_amounts.append(need_amount)
   all_units.append(need_unit)


   # Ask for Total Amount of ingredient purchased
   total_amount, total_unit, total_amount_in_g = amount_analyser(ing_name, "Total Ingredient Amount: ")
  

   #Ask for Ingredient Price
   ing_price = float_checker("Ingredient Price: $", "price")
   
   #Calculate cost of ingredient needed
   calc_ing_cost()

   space(1)

#Calculate cost per serving
cost_per_serving = calc_serving_cost()

#Output results
print("Total cost is {}".format(cost_per_serving))

   
 