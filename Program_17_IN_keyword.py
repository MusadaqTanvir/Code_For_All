#creating the list ..
Fruits = ['Apples','Bananas','Mangoes','Grapes']
user_fruit = 'Bananas'
if user_fruit in Fruits:
    print("Available :)")
else:
    print("Sorry, This is not Available :(")
user_b = 'Strawberry'
if user_b not in Fruits:
    print(f"Sorry, Your request food {user_b} is not in the stock :(" )