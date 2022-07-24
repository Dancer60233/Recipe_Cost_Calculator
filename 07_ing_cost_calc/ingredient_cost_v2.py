#16/7/22 - KLB
#Recipe Cost Calculator
#Ingredient Cost Calculation V2
#Aim - To add functions to my code and fix the formating on my recipe cost output


#Functions
def ing_cost_calc(price, need_ing, total_ing):
  ing_cost = (price/total_ing) * need_ing
  return ing_cost

#Main Routine 

#intialise recipe cost variable
recipe_cost = 0

#Repeat 3 times for testing
for item in range(3):

  #Get input
  price = float(input("Ingredient Price: "))
  need_amount = float(input("Needed Amount: "))
  total_amount = float(input("Total Amount: "))

  #Calculate cost and print
  ing_cost = ing_cost_calc(price, need_amount, total_amount)
  print(ing_cost)
  print("")
  recipe_cost += ing_cost
  

print("Recipe Cost: {:.2f}".format(recipe_cost))
  
