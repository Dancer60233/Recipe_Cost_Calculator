#14/6/22 - KLB
#Recipe Cost Calculator
#Recipe not blank V1
#Aim - To get a basic version of recipe not blank 


#Functions   
def not_blank(question):
  valid = False

  while not valid:
    response = input(question)

    if response != "":
      return response

    else:
      print("Sorry - this can't be blank, "
            "please enter your recipe name")

#Main Routine


name= not_blank("Recipe: ")
  
     