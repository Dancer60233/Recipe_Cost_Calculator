#8/7/22 - KLB
#Recipe Cost Calculator
#Gram Conversion V1
#Aim - To create a basic version of the gram conversion component that works

def gram_conversion(amount, unit):
 if unit == "g":
   gram_amount = amount
 elif unit == "kg":
  gram_amount = amount * 1000
 elif unit == "tsp":
  gram_amount = amount * 5.69
 elif unit == "tbsp":
  gram_amount = amount * 17.07 
 return gram_amount
   



amounts = 5
units = "tbsp"

amount_in_g = gram_conversion(amounts, units)

print("Ingredient amount: {} {}".format(amounts,units))
print("Amount in Grams: {}g".format(amount_in_g))