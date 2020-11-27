list = []

# add objects into this empty list
list.append(5)
list.append(13)
list.append(6)
list.append(27)
list.append(10)

print(list)

# method that inserts object into position (pos, object)
list.insert(0, 3)
list.insert(1, 27)

print(list)
print(list.count(27)) # returns the number of entries matching this object
print(list.index(27)) # returns index position of first entry matching this object

print('location of all 27s:')
for loc in range(len(list)):
    if list[loc] == 27: print('**:', loc)

list.reverse() # reverse the order of objects in the list
print(list)
list.reverse()

list.sort() # sort the objects in the list
print(list)

list.remove(27) # removes first occurance (L to R) of this object from the list
print(list)
list.remove(list[3]) # removes this object at [location] from the list
print(list)
del list[-1] # removes the object at location specified
print(list)

last = list.pop() # removes the (arg location) object from the list and returns it. no arg = last
print(list)
print(last)
