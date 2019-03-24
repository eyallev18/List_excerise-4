"""
This is Exercise in List
written by Eyal Lev
Date March 24st 2019
"""

myUniqueList=[]  # list declaration &  initialization
myLeftover=[]       # list declaration & initialization


def add_thing(thing):
    if thing not in myUniqueList:  # check if the "thing" in lis
        myUniqueList.append(thing)  # if not add it at the end
        return True
    else:
        myLeftover.append(thing)     # if not in list reject adding and add to "myLeftover" list
        return False


def print_add_new_value(value):
    print('New Value is:' ,value, " , it's none existing  item: ", add_thing(value), ",  myUniqueList is: ",myUniqueList," , myLeftover is: ", myLeftover," .")


print_add_new_value(2)
print_add_new_value(3)
print_add_new_value(4)
print_add_new_value(2)
print_add_new_value(5)
print_add_new_value(6)
print_add_new_value(3)
print_add_new_value(7)
print_add_new_value(8)
print_add_new_value(7)
