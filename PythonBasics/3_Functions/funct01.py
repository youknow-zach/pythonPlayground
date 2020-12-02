# basic definition of a function
# this code defines. It does not 'run' the function code automatically
def hello():
    '''This is a 'docstring' that is a descriptor of the function.
    This function says hello and greets you.'''
    print('Hello!\n')

def greetUser():
    '''This function greets the user by name'''
    name = input('What is your name?  ')
    print('Hello, {}!'.format(name))
    print('Glad to meet you!\n')

# this is invoking a function
hello()
print('We are here\n')
greetUser()

# fun fact: you can invoke the function's docstring like so
print(hello.__doc__)

# here is a function that receives a parameter
def square(num):
    '''Square the integer passed into this function (parm**2)'''
    sq = num**2
    print('\n{} is the square of {}\n'.format(sq, num))

# invoking the function
square(10)

# here is a function that takes parameters and returns a value
def factor(n):
    '''Generate a list of the factors of the int passed into this function'''
    testlist = list(range(1, n))
    factors = []
    for num in testlist:
        if n%num == 0: factors.append(num)
    return factors
    # this returns variable 'factors' and terminates the function
    # when a function hits a return, it returns to the invocation                

# invoking the function
testvalue = 12
results = factor(testvalue)
print('The factors of {} are: {}'.format(testvalue, results))
