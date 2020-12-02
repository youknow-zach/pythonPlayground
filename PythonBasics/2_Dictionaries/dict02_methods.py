# random dictionary
inventory = {'apples':216, 'bananas':601, 'pears':128, 'oranges':405, 'cherries':540}
print('\n{}\n'.format(inventory))

# printing length and key/value pairs
numItems = len(inventory)
print('number of fruit:', numItems)

# .keys() returns an object that can be iterated over
for key in inventory.keys():
    print(key+':', inventory[key])

# iterating over a dicitonary implicitly iterates over its keys
print('')
for item in inventory:
    print('We have {} {}!'.format(inventory[item], item))

# putting the keys into a list requires the list function
# .keys() does not return a list directly
fruit = list(inventory.keys())
print('\n{}\n'.format(fruit))

# here are complimentary methods for .keys() to print the values
# and print the key/value pairs as tuples
print(inventory.keys())
print(inventory.values())
print(inventory.items())
print('')

# .items() can be used in an iterative loop similarly
for k in inventory.items():
    print(k)

# can use 'in' expression to test for presence of keys
print('\nbananas?', 'bananas' in inventory, '\n')
if 'oranges' in inventory:
    print('We have', inventory['oranges'], 'oranges')
    if 'pineapples' in inventory:
        print('Aaaand we have', inventory['pineapples'], 'pineapples!!\n')
    else: print('But we have no pineapples\n')
else:
    print('We have no oranges')
    if 'pineapples' in inventory:
        print('But we have', inventory['pineapples'], 'pineapples!\n')
    else: print("And we have no freakin' pineapples!?\n")

# .get() is diff from indexing
# if you don't have the key you reference, your return is 'None'
print(inventory.get('pineapples'))

# you can pass an argument to change the return fail value
print(inventory.get('pineapples', 'No pineapples'))
print('How many pineapples do we have? {}'.format(inventory.get('pineapples', 0)))
