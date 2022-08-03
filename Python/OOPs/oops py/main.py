from Items import Items
from phone import phone


# If we want restrict to change intialise attribute of class Items then use encapulations 

# item1=Items("MyItems",750)
# item1.name="OtherItems"

# print(item1.name) ## if we are run the code our items name is changed... so can we we do that to dont access to change

# print(item1.read_only_name) # print the value of "AAA"
#item1.read_only_name="BBB" # got error if we are trying to overload the attribute because it is read only under property


item1=Items("MyItems",750)
# item1.__name="Other things"
print(item1.name)
