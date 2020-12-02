pir_dict = {'sir':'matey', 'hotel':'fleabag inn', 'student':'swabbie',
            'boy':'matey', 'madam':'proud beauty', 'professor':'foul blaggart',
            'restaurant':'galley', 'your':'yer', 'excuse':'arr',
            'students':'swabbies', 'are':'be', 'lawyer':'foul blaggart',
            'the':"th’", 'restroom':'head', 'my':'me',
            'hello':'avast', 'is':'be', 'man':'matey'}

for engword, pirword in pir_dict.items():
    print(engword, pirword)

string = input("Give me a sentence, Matey!:  ")
str_words = string.split()
for word in range(len(str_words)):
    if str_words[word] in pir_dict:
        str_words[word] = pir_dict[str_words[word]]

pir_string = ''
#print(str_words)
for newword in str_words:
    pir_string += newword + ' '

print(pir_string)
