#8/7/22 - KLB
#Recipe Cost Calculator
#Gram Conversion V2
#Aim - To create a basic version of the gram conversion component that involves cups for basic ingredients

def gram_conversion(amount, unit, ingredient):
#Convert different units to grams
 if unit == "g":
   gram_amount = amount
 elif unit == "kg":
  gram_amount = amount * 1000
 elif unit == "tsp":
  gram_amount = amount * 5.69
 elif unit == "tbsp":
  gram_amount = amount * 17.07 
 elif unit == "cups":
  #More precise for different ingredients
  if ingredient == "Butter" or ingredient == "Sugar":
   gram_amount = amount * 250
  elif ingredient == "Flour":
   gram_amount = amount * 125
  elif ingredient == "Oil":
   gram_amount = amount * 220
  elif ingredient == "Water":
   gram_amount = amount * 236 
  else:
    gram_amount = amount * 250
 return gram_amount
   


#repeat 6 times for testing 
for item in range(6):
 amount = int(input("Amount: "))
 unit = input("Unit: ")
 ingredient = input("Ingredient: ")

 amount_in_g = gram_conversion(amount, unit, ingredient)

#Print details...
 print("Ingredient: {} ({} {})".format(ingredient,amount,unit))
 print("Amount in Grams: {}g \n".format(amount_in_g))