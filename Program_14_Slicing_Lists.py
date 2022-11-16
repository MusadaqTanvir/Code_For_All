#creating the list of Numbers first

Numbers = list(range(1,21))
print("The List of Numbers are\n", Numbers)

#Slicing through the List

Subset_Numbers = Numbers[1:10]
print("The Second Sliced List\n",Subset_Numbers)

#Another Slice
Sub_Num = Numbers[2:8]
print("The Third sliced list\n", Sub_Num)

#Negative Slicing or from the right to left..
# Here the Concept of Colon and negative indexing shows that it starts couting from 
List_2 = Numbers[:-10] # it will skip 10 index from the right as it is on the right side of colon(:)
print("Negative Slicing\n", List_2)

List_3 = Numbers[-10:] # it will skip first 10 index as it is written on the left side of colon(:)
print("The Right 10 index of List\n", List_3)