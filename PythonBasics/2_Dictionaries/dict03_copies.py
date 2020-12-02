# asigning a dictionary to another dictionary makes them the same
opposites = {'up': 'down', 'right': 'wrong', 'true': 'false'}
alias = opposites

print(alias is opposites)

alias['right'] = 'left'
print(opposites['right'], '\n')

# if you want to copy a dictionary you must use the copy method
colors = {'red':3, 'blue':6, 'green':5, 'yellow':9}
hues = colors.copy()

print(colors is hues)

hues['purple'] = 4
print(colors)
print(hues)
