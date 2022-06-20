#20/6/22 - KLB
#Recipe Cost Calculator
#Base V2
#Aim - To add my not blank function to the code


#------------Functions---------------

def not_blank(question):
  valid = False

  while not valid:
    response = input(question)

    if response != "":
      return response

    else:
      print("Sorry - This can't be blank")




def float_checker(input):
 print("Place holder")

def string_analyser(input):
 print("Place holder")

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

if __name__ == "__main__":

 #Welcome users
 print("Welcome to the Recipe Cost Calculator")

#Ask user for basic details about recipe
 recipe_name = not_blank("Recipe Name:")
 serving_size = input("Sering Size:")
 serving_size = float_checker(serving_size)
 space(2)

#Loop for number of ingredients
 for item in range(0, num_ing):
   
   #Ask for information about ingredients

   #Ingredient name 
   ing_name = not_blank("Ingredient Name: ")

   #Amount of ingredient needed
   amount_ing_need = input("Amount Ingredient Needed:")
   amount_ing_need = string_analyser(amount_ing_need)

   #Total Amount of ingredient purchased
   total_amount_ing = input("Total Amount of Ingredient Purchased:")
   total_amount_ing = string_analyser(total_amount_ing)

   #Ingredient Price
   ing_price = input("Ingredient Price:")
   ing_price = float_checker(ing_price)
   
   #Calculate cost of ingredient needed
   calc_ing_cost()

   space(1)

#Calculate cost per serving
 cost_per_serving = calc_serving_cost()

#Output results
 print("Total cost is {}".format(cost_per_serving))

   
 