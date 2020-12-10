# Mapping

# Here is a previous example of how we would map a list to another list and double all elements
def doubleStuff(a_list):
    """ Return a new list in which contains doubles of the elements in a_list. """
    new_list = []
    for value in a_list:
        new_elem = 2 * value
        new_list.append(new_elem)
    return new_list

things = [2, 5, 9]
print(things)
things = doubleStuff(things)
print(things)

# Using the map function, you can pass a funtion as a mapping parameter
def triple(value):
    return 3*value

def tripleStuff(a_list):
    new_seq = map(triple, a_list)
    return list(new_seq)

def quadrupleStuff(a_list):
    new_seq = map(lambda value: 4*value, a_list)
    return list(new_seq)

things = [2, 5, 9]
things3 = tripleStuff(things)
print(things3)
things4 = quadrupleStuff(things)
print(things4)

# Of course, once we get used to using the map function, it’s no longer necessary
# to define functions like tripleStuff and quadrupleStuff
things5 = map((lambda value: 5*value), things)
print(list(things5))

# Or all on one line
print(list(map((lambda value: 6*value), [1, 2, 3])))

# Another example
abbrevs = ["usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", "jam"]
print(list(map(lambda place: place.upper(), abbrevs)))
