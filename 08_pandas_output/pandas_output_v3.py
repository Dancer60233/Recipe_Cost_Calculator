#18/7/22 - KLB
#Recipe Cost Calculator
#Pandas Output V3
#Aim - Print out all information mostly using pandas to produce it in a nicer way then previously.

import pandas

#Initialise Snack Lists
#Data already inside for testing purposes
all_ing_names = ["Butter", "Flour"]
all_prices = [5, 1.67]
all_need_amounts= ["100 g", "1 cup"]
all_total_amounts = ["500 g", "1.5 kg"]
all_ing_costs = [1, 0.14]


#Data already included for testing purposes
recipe_name = "Cookies"
serving_size = 2.5
total_cost = 5
cost_per_serving = 2


#Data Frame Dictionary
recipe_cost_dict = {
    'Ingredient Name': all_ing_names,
    'Price': all_prices,
    'Amount Needed': all_need_amounts,
    'Amount Total': all_total_amounts,
    'Ingredient Cost': all_ing_costs,
    }



ingredients_frame = pandas.DataFrame(recipe_cost_dict)
ingredients_frame = ingredients_frame.set_index('Ingredient Name')

#set up columns to be printed
pandas.set_option('display.max_columns', None)

#Display numbers to 2 dp
pandas.set_option('display.precision', 2)

#Rename columns to shorter names
ingredients_frame = ingredients_frame.rename(columns={'Amount Needed': 'Amount', 'Ingredient Cost': 'Cost'  })


#print details...
print("\n{}     Serving Size: {}  \n".format(recipe_name, serving_size))
print(ingredients_frame[['Amount', 'Cost']])
print("\nTotal Cost: {:.2f} \nCost per serving: {:.2f}".format(total_cost, cost_per_serving))
