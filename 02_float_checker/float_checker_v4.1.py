#15/6/22 - KLB
#Recipe Cost Calculator
#Float Checker V4.1
#Aim - To create a function that still has specific error messages but would be more flexible when the function is used for different questions


def float_checker(question, string_error_message, neg_num_error_message): 
  valid = False
  while not valid:

   #ask user for number and checks if it is valid
   try:
    response = float(input(question))

    if response > 0:
      valid = True
   #Checks if number is in range
    else:
     print(neg_num_error_message)
   except:
     print(string_error_message)

  return response
      





# Main Routine 
serving_size = float_checker("Serving size: ", "Invalid number! Please enter the serving size as a number", "Negative Number! Please enter a valid serving size")
print(serving_size)