# creating the pizza dictionary
pizza = {'crust':'thick',
         'topping':['mushrooms','extra cheese']
         }
print(f"You Pizza is being prepared with {pizza['crust']}-crust")
for toping in pizza['topping']: # the toping will return the list of values and the loop will be iterate through these values of lists. 
    print("\t",toping)