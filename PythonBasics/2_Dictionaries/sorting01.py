tups = [('A', 3, 2),
        ('C', 1, 4),
        ('B', 3, 1),
        ('A', 2, 4),
        ('C', 1, 2)]
for tup in tups:
    print(tup)

print('Sorted:')
for tup in sorted(tups): # sorting based on sequential object in tuple
    print(tup)

print('Sorted in order (#2, #3, #1):')
# sorting based on last item, then first item, then middle item (look at lambda)
for tup in sorted(tups, key=lambda new_tup: (new_tup[2], new_tup[0], new_tup[1])):
    print(tup)

fruits = ['peach', 'kiwi', 'apple', 'blueberry', 'papaya', 'mango', 'pear']
# creating a list with a new sort order based on the fruit name length
# then alpha of fruit names
new_order = sorted(fruits, key=lambda fruit_name: (len(fruit_name), fruit_name))
print(type(new_order))
for i in new_order:
    print(i)
for fruit in new_order:
    print(fruit)
