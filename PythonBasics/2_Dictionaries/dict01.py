# dictionary started with curly braces
eng2fr = {}
eng2fr['one'] = 'un'
eng2fr['two'] = 'deux'
eng2fr['three'] = 'trois'
eng2fr['four'] = 'quatre'

print('\n\neng2fr dict:', eng2fr)

# dictionaries can all be set on one line as well
eng2sp = {'one':'uno', 'two':'dos', 'three':'tres', 'four':'quatro'}

print('eng2sp dict:', eng2sp)

# here's how you look up a value
value = eng2fr['one']
print('\n' + value)
print(eng2fr['two'])

# random dictionary
inventory = {'apples':216, 'bananas':601, 'pears':128, 'oranges':405, 'cherries':540}
print('\n{}\n'.format(inventory))

# here's how you remove
del inventory['oranges']
print('**stopped stocking oranges**\n{}\n'.format(inventory))

# re-adding oranges
inventory['oranges'] = 214
print('**added more oranges**\n{}\n'.format(inventory))

inventory['oranges'] = inventory['oranges'] + inventory['oranges']
print('**doubled oranges**\n{}\n'.format(inventory))

numItems = len(inventory)
print('number of fruit:', numItems)

for key in inventory.keys():
    print(key+':', inventory[key])
