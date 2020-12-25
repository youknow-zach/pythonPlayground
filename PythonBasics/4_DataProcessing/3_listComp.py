# List Comprehension


# Mapping a list with list comprehension
things = [2, 5, 9]

yourlist = [value * 2 for value in things]

print(yourlist)

# Filtering a list with list comprehension
def keep_evens(nums):
    new_list = [num for num in nums if num % 2 == 0]
    return new_list

print(keep_evens([3, 4, 6, 7, 0, 1]))

# Combining Mapping and Filtering operations in list comprehension
things = [3, 4, 6, 7, 0, 1]

# First, filter to keep only the even numbers
# Double each of them
print(map(lambda x: x*2, filter(lambda y: y % 2 == 0, things)))

# Equivalent version using list comprehension
print([x*2 for x in things if x % 2 == 0])
