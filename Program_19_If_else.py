#creating the two list
Available_topings = ['mushroms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_topings = ['mushroms','french fries','extra cheese']
for requested_toping in requested_topings:
    if requested_toping in Available_topings:
        print(f"We are adding {requested_toping} to Your Pizza")
    else:
        print(f"Sorry: We are out of {requested_toping} right now :(")
print("Finished Your Pizza")
exit()