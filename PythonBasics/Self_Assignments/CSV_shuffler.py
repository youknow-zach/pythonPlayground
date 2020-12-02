import random

def big_slices(lst):
    len_fifth = int(len(lst)/5)

    cycle = 0
    while cycle < 10:
        # copy and remove large segment to shuffle
        slice_start = random.randrange(1, len(lst)-len_fifth)
        slice_end = slice_start + len_fifth
        slice_list = lst[slice_start:slice_end]
        del lst[slice_start:slice_end]

        # find new location to insert the list into
        insert_pos = random.randrange(1, len(lst))
        for item in range(len(slice_list)):
            lst.insert(insert_pos + item, slice_list[item])

        print('I have sliced rows: {} to {}'.format(slice_start, slice_end))
        print('I have inserted it at pos: {}'.format(insert_pos))
        cycle += 1

    return lst

# open csv
csvname = input('CSV name?\n>>  ')
if csvname == '': csvname = 'vgsalesGlobale'

fhandle = open('Data/'+csvname+'.csv', 'r')
data = fhandle.readlines()
line = 0

# print the first 15 lines
while line <= 16:
    print(data[line].strip())
    line += 1

fhandle.close()
data = big_slices(data)


# pick small segments to shuffle
# pick individual lines to shuffle
# save CSV to diff filename
with open('Data/'+csvname+'_shuffle.csv', 'w') as csvsave:
    for entry in data:
        csvsave.write(entry)
