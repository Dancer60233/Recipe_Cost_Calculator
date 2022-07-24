#14/6/22 - KLB
#Recipe Cost Calculator
#Recipe not blank V2
#Aim - To get a basic version of recipe not blank but allow a more customisable error message that can be used for different questions




#Functions   
def not_blank(question, error_message):
  valid = False

  while not valid:
    response = input(question)

    if response != "":
      return response

    else:
      print(error_message)

#Main Routine

#print details...
name= not_blank("Recipe: ", "Sorry- this can't be blank, please enter your recipe name")
  