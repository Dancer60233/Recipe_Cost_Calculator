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

#loop 7 times to make testing quicker

for item in range (0,7):
   desired_unit = input("Unit: ").lower()

   for var_list in valid_units:
   #if unit is in one of the lists, return the shorthand
    if desired_unit in var_list:
  #Get shorthand of unit and put it in lowers case so it looks nice when outputted
     unit = var_list[0].lower()
     unit_valid = True
     break
    

    else:
      unit_valid = False

    #if the unit is not OK - ask question again
   if unit_valid == True:
     print("Unit Choice: ",unit)

   else:
      print("Invalid choice")

    
 


