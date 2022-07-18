#17/7/22 - KLB
#Recipe Cost Calculator
#Pandas Output V1
#Aim - To create a basic table that doesn't include the title or total to set up the basic dictionary

import pandas

#Initialise Snack Lists
#Data already inside for testing purposes
all_ing_names = ["butter", "flour"]
all_prices = [5, 1.67]
all_need_amounts= ["100 g", "1 cup"]
all_total_amounts = ["500 g", "1.5 kg"]
all_ing_costs = [1, 0.14]


#Data Frame Dictionary
recipe_cost_dict = {
    'Ingredient Name': all_ing_names,
    'Price': all_prices,
    'Amount Needed': all_need_amounts,
    'Amount Total': all_total_amounts,
    'Ingredient Cost': all_ing_costs,
    }

#print details...
recipe_cost_frame = pandas.DataFrame(recipe_cost_dict)
recipe_cost_frame = recipe_cost_frame.set_index('Ingredient Name')
print(recipe_cost_frame)