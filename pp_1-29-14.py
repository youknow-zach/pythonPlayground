#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
name = input("What is your name? ")

while True:
    age = input("What is your age? ")
    try:
        age = int(age)
    except:
        print("That is not a valid age")
        continue
    if age < 1:
        print("That is not a valid age")
    elif age >= 100:
        print("You're already a centurian!")
    else: break

while True:
    year = input("What is the year? ")
    try:
        year = int(year)
    except:
        print("That is not a valid year")
        continue
    if year < 2020:
        print("That is not a valid year")
    elif year >= 3000:
        print("Wow, this program is really old...")
    else: break

y100 = (100 - age) + year

print("Hello", name, ". Your age is", age, "\ntherefore you will turn 100 in the year", y100)

#Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.
#Print out that many copies of the previous message on separate lines.
