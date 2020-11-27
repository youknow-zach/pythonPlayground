z = ['try', 4, 'dig', 7, 'fizz', 3, 'shirt', 9, 4, 'basic', 0]
print(z.count(4))
print(z[6])
print(z[6].count('i'))

count = 0
for i in range(len(z)):
    try: count += z[i].count('i')
    except: continue

print(count)
