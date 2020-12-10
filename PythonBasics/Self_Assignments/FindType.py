data = []

with open('Data/vgsalesShort.csv', 'r') as file:
    for line in file:
        data.append(line.strip().split(','))

for entry in data:
    del entry[4:10]
    del entry[1]


print(data)
