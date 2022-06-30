#1/7/22 - KLB
#Recipe Cost Calculator
#String Checker V2
#Aim - To create a version of my string checker that allows for the full name and short name of the unit



#lists
valid_units =[
  ["g", "grams" ],
  ["kg", "kilograms"],
  ["tbsp", "tablespoon"],
  ["tsp", "teaspoon"]
]

#Intialise variables

unit_valid = ""
unit = ""

#loop three times to make testing quicker

for item in range (0,7):
   desired_unit = input("Unit: ").lower()

   for var_list in valid_units:
   #if snack is in one of the lists, return the full name
    if desired_unit in var_list:
  #Get full name of snack and put it in titles case so it looks nice when outputted
     unit = var_list[0].lower()
     unit_valid = True
     break
    

  #if the chosen snack is not valid, set snack_ok to 
    else:
      unit_valid = False

    #if the snack is not OK - ask question again
   if unit_valid == True:
     print("Unit Choice: ",unit)

   else:
      print("Invalid choice")

    
 


