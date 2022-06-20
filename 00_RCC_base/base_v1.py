#20/6/22 - KLB
#Recipe Cost Calculator
#Base V1
#Aim - To create a version of my code that has all functions and my basic decomposition. So even though it won't work currently it'll make it easier to add components


#------------Functions---------------

def not_blank(question):
 print(question)

def float_checker(question):
  print(question)

def string_analyser(question):
  print(question)

def calc_ing_cost():
  print("calculate ingredient cost")

def calc_serving_cost():
  print("Cost Per Serving")

def space(num_spaces):
 for item in range (0, num_spaces):
   print()

  





#*************** Main Routine *************

#Temporary number of ingredients will ask user in future versions
num_ing = 3

if __name__ == "__main__":

 #Welcome users
 print("Welcome to the Recipe Cost Calculator")

#Ask user for basic details about recipe
 recipe_name = not_blank("Recipe Name:")
 serving_size = float_checker("Sering Size:")

 space(1)

#Loop for number of ingredients
 for item in range(0, num_ing):
   
   #Ask for information about ingredient
   ing_name = not_blank("Ingredient Name: ")
   amount_ing_need = string_analyser("Amount Ingredient Needed:")
   total_amount_ing = string_analyser("Total Amount of Ingredient Purchased:")
   ing_price = float_checker("Ingredient Price")
   
   #Calculate cost of ingredient needed
   calc_ing_cost()

   space(1)

#Calculate cost per serving
 cost_per_serving = calc_serving_cost()

#Output results
 print("Total cost is {}".format(cost_per_serving))

   
 