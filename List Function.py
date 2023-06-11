# List
# It is a collection of different data
list_1= ["Karan","Raj","Singh",11,11.3,True] # I have added the string, integer, float and Boolean
print(list_1)
# Sllicing of the list to take the elements from the list
print(list_1[0:5:2]) # indicates the first five elements to be selection criteria and we need to take out the every second element.
print(len(list_1)) # to count the number of elements in the list
print(12 in list_1) # Boolean value will be given
# Append, Insert, Remove, Pop
list_1.append(12)
print(list_1)
list_1.insert(0,11)
print(list_1)
list_1.remove("Karan") # name of the data
print(list_1)
list_1.pop(0) # Position number only
print(list_1)

list_2=[2,3,1,5,4,6,7]
list_2.sort(reverse= False)
print(list_2)