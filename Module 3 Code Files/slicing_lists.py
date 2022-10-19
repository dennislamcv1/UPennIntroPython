my_list = ['b', 'a', 'n', 'a', 'n', 'a', 's']

print(my_list[2:5]) #elements 3 - 5

print(my_list[4:]) #elements 5 - end

print(my_list[:]) #elements 1 - end

print(my_list[:-4]) #elements 1 - 3

#true copy of my_list
copy_my_list = my_list[:] #elements 1 - end

print(copy_my_list is my_list) #references to same list?
print(copy_my_list == my_list) #same values?