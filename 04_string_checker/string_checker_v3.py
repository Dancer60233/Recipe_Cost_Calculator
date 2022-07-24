#1/7/22 - KLB
#Recipe Cost Calculator
#String Checker V3
#Aim - To create a version of my string checker with a function 

def string_check(choice, options):

 for var_list in options:
   #if unit is in one of the lists, return the shorthand
      if choice in var_list:
  #Get shorthand of unit and put it in lowers case so it looks nice when outputted
       return var_list[0].lower()
       is_valid = "yes"
       break

      else:
        is_valid = "no"

 if is_valid == "yes":
    return chosen

 else:
    return "invalid choice"





  
#Main Rotuine

#lists
valid_units =[
  ["g", "grams" ],
  ["kg", "kilograms"],
  ["tbsp", "tablespoon"],
  ["tsp", "teaspoon"]
]

unit = "invalid choice"  
while unit == "invalid choice":
 desired_unit = input("Unit: ").lower()
 
 unit = string_check(desired_unit, valid_units)

#Error Message
 if unit == "invalid choice":
   print("Invalid Choice! Please enter a valid unit")
 
#output
print(unit)

