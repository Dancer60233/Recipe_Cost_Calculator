#15/6/22 - KLB
#Recipe Cost Calculator
#Float Checker V1
#Aim - To get a basic version of Float Checker so it only accepts numbers (regardless if their an integer or not)

def float_checker(question, error_message): 
  valid = False
  while not valid:

   #ask user for number and checks if it is valid
   try:
    response = float(input(question))
    valid = True
   #Checks if number is in range
   except:
    print(error_message)

  return response
      





# Main Routine 
serving_size = float_checker("Serving size: ", "Invalid number! Please enter the serving size ")
print(serving_size)