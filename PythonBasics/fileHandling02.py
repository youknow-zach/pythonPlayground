print('This begins the program output**\n\nSect0\n')

# you can open a file in a sub-folder from current directory like this
fileref = open("testDir/romeo.txt", "r")
for line in fileref:
    print(line.strip())
fileref.close()

print('\nSect1\n')

# you can move up in your directory with .. and go to a diff folder like this
fileref = open("../PY4E Examples/romeo.txt", "r")
for line in fileref:
    print(line.strip())
fileref.close()

print('\nSect2\n')

# you can write to a file like this
fileref = open("testDir/writeMe.txt", "w")
write = 0
for num in range(12):
    write = num*num
    #print('written:', write)
    #fileref.write(str(write)+'\n')
fileref.close()
# as soon as the file is loaded in write mode the previous contents are wiped
# every time this code is executed the file will be overwritten

print('\nSect3\n')

# this is a way to open a file. file is closed when with block ends
with open('testDir/writeme.txt', 'r') as file:
    for line in file:
        print(line.strip())
