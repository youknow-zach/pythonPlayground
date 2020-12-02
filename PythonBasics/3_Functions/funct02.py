# functions only return once
def testPrint():
    '''This function tries to print multiple times'''
    print('\nHello!')
    return
    print('\nHello, again!')
    return

# this is invoking a function
testPrint()

# therefore you can nest functions to return in specific situations
def alphaName(n1, n2, n3):
    '''This function returns the name that comes first in alphabetical order'''
    ln1 = n1.lower()
    ln2 = n2.lower()
    ln3 = n3.lower()

    if ln1[0] < ln2[0]:
        if ln1[0] < ln3[0]: return n1
        else: return n3
    else:
        if ln2[0] < ln3[0]: return n2
        else: return n3

firstName = alphaName('Caleb', 'Ralph', 'Andrew')
print(firstName)
