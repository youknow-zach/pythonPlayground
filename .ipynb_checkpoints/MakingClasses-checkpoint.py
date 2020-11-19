#Setting up a basic class
class MyClass:

    # Inherent variable in the class
    variable = 'blah'

    # Inherent function in the class
    def function(self):
        print('This is a message inside the class')

# Creating instances of MyClass objects
myobjectx = MyClass()
myobjecty = MyClass()

# Overwriting the Inherent variable in myobjecty object instance
myobjecty.variable = 'yackity'

# Then print out both values
myobjectx.function()
myobjecty.function()
print(myobjectx.variable)
print(myobjecty.variable)
