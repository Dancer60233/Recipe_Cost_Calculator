#15/6/22 - KLB
#Recipe Cost Calculator
#Float Checker V4.2
#Aim - To create a function that is more flexible for both the serving size and price as you can change the error message. However the code will be more efficent as the string error message will stay the same 


def float_checker(question, error_message): 
  valid = False
  while not valid:

   #ask user for number and checks if it is valid
   try:
    response = float(input(question))

    if response >= 0:
      valid = True
   #Checks if number is in range
    else:
     print(error_message)
   except:
     print("Invalid number! Please enter a valid number")

  return response
      





# Main Routine 
serving_size = float_checker("Serving size: ", "Negative Number! Please enter a valid serving size")
print(serving_size)