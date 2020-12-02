# accumulating with a dictionary
file = open('../testDir/romeo.txt')
txt = file.read() # open store the text contents of the file here
print(txt)
letters = {}

for char in txt:
    char = char.upper() # all letters converted upper so we dont get duplicates ('t' and 'T')
    if char == ' ' or char == '\n': continue # skipping spaces and newlines
    else:
        letters[char] = letters.get(char, 0) + 1

for count in letters.items(): print(count)
file.close()

# opening file with 'with' to iterate over the lines and captures the words
wordDict = {}
with open('../testDir/romeo.txt') as txtlst:
    for line in txtlst:
        hold = line.split()
        for word in hold:
            word = word.lower()
            wordDict[word] = wordDict.get(word, 0) + 1

for entry in wordDict:
    print('{} occurences of {}'.format(wordDict[entry], entry))

# finding the highest occuring letters in dict 'letters'
# note: if there are two highests it will only capture the first
highest = None
for key in letters.keys():
    if highest == None:
        highest = key
        continue
    if letters[highest] < letters[key]:
        highest = key

print(highest)
