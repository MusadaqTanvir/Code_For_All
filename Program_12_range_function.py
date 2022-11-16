#Range function in the python
#simple Range function
from Program_11_For_Loop import My_List


for i in range(0,10):
    print(i)
#Range function that works with step size
for j in range(0, 10, 2):
    print(j)
# Generating the Numbers from 1 to 10 and storing them into the list
My_List = list(range(0, 11))
print(My_List)