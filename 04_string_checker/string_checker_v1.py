#1/7/22 - KLB
#Recipe Cost Calculator
#String Checker V1
#Aim - To attempt to create a basic version of my string analyser without it being in a function

#Functions

def string_check(question, to_check):


  valid = False

  while not valid:

    response = input(question).lower()

    if response in to_check:
      return response

    else:
      for item in to_check:
        #checks if response is the first letter of an item in the list
        if response == item[0]:
          # note:returns the entire response rather than just the first letter
          return item

      print("Sorry that is not a valid response")

    

#Main Routine


for item in range (0,6):
  unit = string_check("Units: ", ["grams", "kilograms"])
  print("Answer Valid, Unit: {} \n".format(unit))
