#15/6/22 - KLB
#Recipe Cost Calculator
#Float Checker V3
#Aim - To create a function that has more specific error messages


def float_checker(question): 
  valid = False
  while not valid:

   #ask user for number and checks if it is valid
   try:
    response = float(input(question))
  #Checks if number is negative
    if response > 0:
      valid = True
  
    else:
     print("Negative Number! Please enter a valid serving size")
      
   #Errror prevention for if a string is entered
   except:
     print("Invalid number! Please enter the serving size as a number")

  return response
      





# Main Routine 

#Output
serving_size = float_checker("Serving size: ")
print(serving_size)