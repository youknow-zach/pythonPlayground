# Zip

# This is our known way of combining a list
L1 = [1, 2, 3]
L2 = [3, 4, 5]
L3 = []
print('{}\n{}'.format(L1, L2))

for i in range(len(L1)): L3.append(L1[i] + L2[i])
print(L3)

# Here is the zip function, which combines the lists items, but in tuples
L4 = list(zip(L1, L2))
print(L4)

# Here is combining them like the iterative function above
L4_sums = []
for (x1, x2) in L4:
    L4_sums.append(x1 + x2)

print(L4_sums)

# Here is combining the zip function and combination into one function
L5 = [x1 + x2 + x3 for (x1, x2, x3) in list(zip(L1, L2, L3))]
print(L5)
