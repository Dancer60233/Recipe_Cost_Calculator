#20/07/22 - KLB
#Recipe Cost Calculator
#Base V8
#Aim - To add in pandas so the ouput looks nicer

import pandas


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

     #Checks number isn't negative
    if response >= 0:
      valid = True
    else:
     print("Invalid! Please enter a valid {}!".format(type))
   except:
     print("Invalid number! Please enter a valid number")

  return response
      

def string_check(choice, options):
 for var_list in options:
   #if unit is in one of the lists, return the shothand of the unit name
      if choice in var_list:
  #Get the shorthand of the unit and put it in lowers so it looks nice when outputted
       return var_list[0].lower()
       is_valid = "yes"
       break

      else:
        is_valid = "no"

 if is_valid == "no":
   return "invalid choice"
   
   
 else:
    return "invalid choice"
  




#Splits amount and units, checks their valid and converts them to grams
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
     
     if m.isdigit() or m == "." or m == "-" or m == "/":
        desired_amount = desired_amount + m

     else:
      desired_unit = desired_unit + m

    #Strip unit and amount
    desired_amount = desired_amount.strip()
    desired_unit = desired_unit.strip().lower()


    #If amount is a fraction convert to decimal
    for m in desired_amount:
      if m == "/":
       desired_amount  = eval(desired_amount)

  #Use string check to see if unit is valid
    unit = string_check(desired_unit, valid_units)


  #Check if Amount is valid
  
    if desired_amount == "":
     amount = "invalid choice"

    else:
     amount = float(desired_amount)
    #Checks if it is a negative amount
    if amount < 0:
      amount = "invalid choice"
     
  #Error Messages

      #Error message if unit and amount invalid
    if unit == "invalid choice" and amount == "invalid choice":
      print("Invalid Choice! Please enter a valid unit and amount")
     
   
       #Error message if just is unit invalid
    elif unit == "invalid choice":
      print("Invalid Choice! Please enter a valid unit")
    #Error message if just amount is invalid
    elif amount == "invalid choice":
      print("Invalid Choice! Please enter a valid amount")

  #Gram Conversion
  #Grams
  if unit == "g":
    calc_amount = amount
  #Kilograms
  elif unit == "kg":
    calc_amount = amount * 1000
    #teaspoons
  elif unit == "tsp":
    calc_amount = amount * 5.69
  #Tablespoons
  elif unit == "tbsp":
    calc_amount = amount * 17.07 
  #Mililiters
  elif unit == "ml":
    if ingredient == "milk":
      calc_amount = amount * 1.04
    else:
       calc_amount = amount
  #Litres
  elif unit == "l":
    if ingredient == "milk":
      calc_amount = amount * 1030
    else:
       calc_amount = amount * 1000
  #Eggs
  elif unit == "eggs":
     calc_amount = amount
  #Cups
   #Different calculations for ingredients so it's more accurate
  elif unit == "cups":
    if ingredient == "milk":
      calc_amount = amount * 240
    elif ingredient == "flour":
      calc_amount = amount * 125
    elif ingredient == "oil":
     calc_amount = amount * 220
    elif ingredient == "water":
     calc_amount = amount * 236 
    else:
      calc_amount = amount * 250
   

 #Format amount so it'll be outputted nice
  output_amount = str(amount) + " " + unit
     
  return calc_amount, output_amount
 


 
#Space function to make formatting easier
def space(num_spaces):
 for item in range (0, num_spaces):
   print()

  





#*************** Main Routine *************



#Initialise Ingredient Information Lists
all_ing_names = []
all_prices = []
all_need_amounts= []
all_total_amounts = []
all_ing_costs = []

#Data Frame Dictionary
ingredient_info_dict = {
    'Ingredient Name': all_ing_names,
    'Price': all_prices,
    'Amount Needed': all_need_amounts,
    'Amount Total': all_total_amounts,
    'Ingredient Cost': all_ing_costs,
    }

#List of valid units
valid_units =[
  ["g", "grams", "gram" ],
  ["kg", "kilograms", "kilogram", "kilos", "kilo"],
  ["tbsp", "tablespoon", "tablespoons"],
  ["tsp", "teaspoon", "teaspoons"],
  ["ml", "millilitre", "millilitres"],
  ["l", "litre", "litres", "liter", "liters"],
  ["cups", "cup"],
  ["eggs", "egg"]
]

#Set up Recipe Cost
recipe_cost = 0

if __name__ == "__main__":

 #Welcome users
 print("Welcome to the Recipe Cost Calculator")

#Ask user for basic details about recipe
 recipe_name = not_blank("Recipe Name: ")
 serving_size = float_checker("Serving Size: ", "serving size")
  
 space(1)

print("Please enter all your ingredients and their information\nWhen you have entered all your ingredients enter xxx")

space(1)

ing_name = ""

#Loop until exit code is entered
while ing_name != "xxx":

   

   #Ask for Ingredient name (Check It's not blank)
   ing_name = not_blank("Ingredient Name: ").lower()

  #If exit code is entered break loop
   if ing_name == "xxx":
     break
   else:
     #If name not exit code append Name to list
     all_ing_names.append(ing_name.title())

   
   #Ask for Amount of ingredient needed and analyse it
   need_amount_calc, ing_need_amount = amount_analyser(ing_name, "Amount Needed: ")
  #Add correctly formatted amount to list
   all_need_amounts.append(ing_need_amount)
   


   # Ask for Total Amount of ingredient purchased
   total_amount_calc, ing_total_amount = amount_analyser(ing_name, "Total Amount Bought: ")
  #Add correctly formatted amount to list
   all_total_amounts.append(ing_total_amount)

   #Ask for Ingredient Price
   ing_price = float_checker("Ingredient Price: $", "price")
   #Add correctly formatted amount to list
   all_prices.append(ing_price)
  
   #Calculate cost of ingredient needed and append to list
   ing_cost = (ing_price / total_amount_calc) * need_amount_calc
   all_ing_costs.append(ing_cost)

  #Work out recipe cost
   recipe_cost += ing_cost
   
   space(1)
   
   
space(2)

#Calculate cost per serving
cost_per_serving = recipe_cost / serving_size

#Set up Data Frame Details
ingredients_frame = pandas.DataFrame(ingredient_info_dict)
ingredients_frame = ingredients_frame.set_index('Ingredient Name')

#set up columns to be printed
pandas.set_option('display.max_columns', None)

#Display numbers to 2 dp
ingredients_frame['Ingredient Cost'] = ingredients_frame['Ingredient Cost'].apply(lambda x: float("{:.2f}".format(x)))



#Rename columns to shorter names
ingredients_frame = ingredients_frame.rename(columns={'Amount Needed': 'Amount', 'Ingredient Cost': 'Cost'})
  


#print results..
print("\n{}     Serving Size: {}  \n".format(recipe_name, serving_size))
print(ingredients_frame[['Amount', 'Cost']])
print("\nTotal Cost: {:.2f} \nCost per serving: {:.2f}".format(recipe_cost, cost_per_serving))


   
 