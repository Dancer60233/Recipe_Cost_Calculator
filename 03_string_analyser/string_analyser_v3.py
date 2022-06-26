#20/6/22 - KLB
#Recipe Cost Calculator
#String Analyser V3
#Aim - To attempt to create a basic version of my string analyser without it being in a function


#************** Main Routine ****************

desired_amount = ""
desired_unit = ""
all_amounts = []
all_units = []


for i in range (4):
  ingredient_amount = input("Ingredient Amount: ")
  for m in ingredient_amount:
    if m.isdigit():
        desired_amount = desired_amount + m
        
    else:
      desired_unit = desired_unit + m
      
  desired_unit = desired_unit.strip()
  desired_amount = desired_amount.strip()
  print(desired_amount) 
  print(desired_unit)
  print("Length of Unit:", len(desired_unit))

  



#print order
 


   