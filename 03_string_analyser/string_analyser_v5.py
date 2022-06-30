
  #20/6/22 - KLB
#Recipe Cost Calculator
#String Analyser V5
#Aim - To add the desired unit and amounts to seperate list and get the program to work 


#************** Main Routine ****************




def amount_analyser():
  desired_amount = ""
  desired_unit = ""

  ingredient_amount = input("Ingredient Amount: ")
  for m in ingredient_amount:
    if m.isdigit() or m == ".":
        desired_amount = desired_amount + m
        
    else:
      desired_unit = desired_unit + m
      
  desired_unit = desired_unit.strip()
  desired_amount = desired_amount.strip()
  return desired_amount, desired_unit
 
  

  



#Main Routine

all_amounts = []
all_units = []

#Ask for 4 amounts (repeats 4 times for testing)
for item in range(4):

  #Ask and spilt amount and unit
  desired_amount, desired_unit = amount_analyser()
  all_amounts.append(desired_amount)
  all_units.append(desired_unit)

print("\n")

#Print out unit and amount seprately
number = 0
for amount in all_amounts:
  
  print("Amount: {},   Unit: {}".format(amount, all_units[number]))
  number += 1
   