#20/6/22 - KLB
#Recipe Cost Calculator
#String Analyser V4
#Aim - To contiue on from my V3 code and add it to a function so the code actualy works


#************** Main Routine ****************




def amount_analyser():
  desired_amount = ""
  desired_unit = ""

  ingredient_amount = input("Ingredient Amount: ")
  for m in ingredient_amount:
    if m.isdigit():
        desired_amount = desired_amount + m
        
    else:
      desired_unit = desired_unit + m
      
  desired_unit = desired_unit.strip()
  desired_amount = desired_amount.strip()
  return desired_amount, desired_unit
 
  

  



#Main Routine

all_amounts = []
all_units = []
 
for item in range(4):
  desired_amount, desired_unit = amount_analyser()
  print(desired_amount) 
  print(desired_unit)
  print("Length of Unit:", len(desired_unit))
   