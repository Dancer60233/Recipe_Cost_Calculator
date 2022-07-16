#16/7/22 - KLB
#Recipe Cost Calculator
#Ingredient Cost Calculation V1
#Aim - To create a basic version of the ingredient cost calculator that works without functions

#Main Routine 

  
recipe_cost = 0

for item in range(3):
  price = float(input("Ingredient Price: "))
  need_amount = float(input("Needed Amount: "))
  total_amount = float(input("Total Amount: "))
  ing_cost = (price/total_amount) * need_amount
  print(ing_cost)
  print("")
  recipe_cost += ing_cost

print(recipe_cost)
  
