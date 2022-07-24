#15/6/22 - KLB
#Recipe Cost Calculator
#Float Checker V2
#Aim - To get my previous version of float checker to not accept negative numbers


def float_checker(question, error_message): 
  valid = False
  while not valid:

   #ask user for number and checks if it is valid
   try:
    response = float(input(question))

     #Checks if number is in range
    if response > 0:
      valid = True

    #If needed print out errors
    else:
     print(error_message)
   except:
     print(error_message)

  return response
      





# Main Routine 
#Output
serving_size = float_checker("Serving size: ", "Invalid number! Please enter the serving size ")
print(serving_size)