print('This begins the program output**\n\nSect0\n')

# you can open a file and save the entire contents as a string like this
fileref = open("testfile.txt", "r")
contents = fileref.read()
print(contents[:200])
fileref.close()

print('\nSect1\n')

# this does the same as above, but passing the length as an argument so the
# whole file isn't returned in the string
fileref = open("testfile.txt", "r")
contents = fileref.read(200)
print(contents)
fileref.close()

print('\nSect2\n')

# you can open a file and save the lines as strings within a list this
fileref = open("testfile.txt", "r")
contents = fileref.readlines()
for line in contents[:4]:
    print(line.strip())
fileref.close()

print('\nSect3\n')

# this is the same thing, just printing the list directly from the file
fileref = open("testfile.txt", "r")
it = 0
for line in fileref.readlines():
    if it == 4: break
    print(line.strip())
    it += 1
fileref.close()

print('\nSect4\n')

# the file object supports iteration over itself like this.
# you can't use slicing with brackets [] like a list
fileref = open("testfile.txt", "r")
it = 0
for line in fileref:
    if it == 4: break
    print(line.strip())
    it += 1
fileref.close()

print('\nEnd\n')

# reading over the file object itself is the most common way you'll read files.
# use .readlines if you want to control the number of lines in the output easily
# or if you want to get the number of lines in the file with len().
