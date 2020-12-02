print('This begins the program output**\n\nSect0\n')

# you can open a file in a sub-folder from current directory like this
info = []
with open("../testDir/birthday.csv", "r") as file:
    for line in file:
        print(line.strip())
        info


print('\nSect1\n')

names = [('Tom', 36, 'Baseball'),
        ('Frank', 28, 'Frisbee'),
        ('Jerry', 32, 'Football'),
        ('Harold', 40, 'Basketball')]

file = open('../testDir/writeMe.csv', 'w')

print('writing file **')
header = 'name,age,favorite sport\n'
file.write(header)
print(header)

for entry in names:
    text = '{},{},{}'.format(entry[0], entry[1], entry[2])
    file.write(text + '\n')
    print(text)

file.close()
