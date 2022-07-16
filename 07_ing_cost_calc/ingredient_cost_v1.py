#16/7/22 - KLB
#Recipe Cost Calculator
#Ingredient Cost Calculation V1
#Aim - To create a basic version of the ingredient cost calculator that works

def ing_cost_calc(price, need_ing, total_ing):
  ing_cost = (price/total_ing) * need_ing
  return ing_cost


recipe_cost = 0

for item in range(3):
  price = input("Ingredient Price: ")
  need_amount = input("Needed Amount: ")
  total_amount = input("Total Amount: ")

  ing_cost = ing_cost_calc(price, need_amount, total_amount)
  print(ing_cost)
  recipe_cost += ing_cost

print("Recipe Cost: {}".format(recipe_cost))
  
