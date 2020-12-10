# Filtering
# Going through a list and keeping only those items that meet certain criteria.

# Our thus learned method of filtering a list
def keep_evens(nums):
    new_list = []
    for num in nums:
        if num % 2 == 0:
            new_list.append(num)
    return new_list

print(keep_evens([3, 4, 6, 7, 0, 1]))

# Filter uses a function and a sequence to populate a new sequence for the
# entries that return true in the operation
def keep_evens(nums):
    new_seq = filter(lambda num: num % 2 == 0, nums)
    return list(new_seq)

print(keep_evens([3, 4, 6, 7, 0, 1]))

lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']
print(list(filter(lambda fruit: 'w' in fruit, lst_check)))

# You can chain maps and filters together
things = [3, 4, 6, 7, 0, 1]
# First, filter to keep only the even numbers
# double each of them
print(list(map(lambda x: x*2, filter(lambda y: y % 2 == 0, things))))
