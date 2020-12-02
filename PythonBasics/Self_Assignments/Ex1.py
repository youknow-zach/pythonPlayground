def start_menu():
    # prompt user for the name of the file
    while True:
        fname = input('Please input the name of your file\n(quit)(test)\n>>  ')
        if fname == 'test':
            fname = 'Data/vgsalesGlobale.csv'
            break
        elif fname == 'quit': quit()
        else: print('\nERROR: entry not recognized\n')
    print('Reading file:  ', fname)
    return fname

# this will be the sub-menu for when a user chooses to generate a report
def menu_sub_report():
    while True: # input loop for getting year range
        print('What year(s)?')
        print('(valid input format: YYYY, YYYY-YYYY)(all)(cancel)')
        ryear = input('>>  ')

        if ryear == 'cancel': break
        elif ryear == 'most units':
            report(data_list)
            break
        elif ryear == 'total units':
            print('total units WIP')
            break
        else: print('\nERROR: entry not recognized\n\n')

def tag_columns(hdr, lst):
    columns = {}
    hdr_str = ''

    # go through each column name in hdr and add it into the dict
    for field in range(len(hdr)):
        columns[hdr[field]] = field
        if field == len(hdr)-1: hdr_str += hdr[field]
        else: hdr_str += hdr[field] + ' : '
        # TO-DO: for each of the first 5 rows, do a type test

    print('headers:\n' + hdr_str)

def print_data():
    print(headers)
    # print the data
    for entry in data_list:
        print(entry)

def sort_title(lst):
    # sort list by name (value 1). year then publisher are tie breaker
    title_lst = sorted(lst, key=lambda row: (row[1], row[3], row[5]))
    print('Data sorted by title:')
    for entry in title_lst:
        print('{}, release in {} by {}, sold {}M units'.format(entry[1], entry[3], entry[5], entry[-1]))
        #print(entry)

def sort_year(lst):
    # sort list by year (value 3). name then publisher are tie breakers
    year_lst = sorted(lst, key=lambda row: (-int(row[3]), row[1], row[5]))
    print('\nData sorted by year:')
    for entry in year_lst:
        print('{}: {} sold {}M units'.format(entry[3], entry[1], entry[10]))

def report_unit_most(lst):
    # sort list by most units (value -1). name then year are tie breakers
    report_lst = sorted(lst, key=lambda row: (-float(row[10]), row[1], row[3]))
    print('\nData sorted by units sold:')
    for entry in report_lst:
        print('{}M units sold by {}'.format(entry[10], entry[1]))

def report_unit_total(lst):
    # init variables
    unit_total = 0
    game_list = []
    str_games = ''
    report_year = input('\nWhat year?\n>>  ')

    # checking each entry for matching year:
    # adding units to total, adding name to game_list
    for entry in lst:
        if entry[3] == report_year:
            unit_total += float(entry[10])
            game_list.append(entry[1])

    # putting game names in string for print output formatting
    for game in range(len(game_list)):
        if game == len(game_list)-1: str_games += game_list[game]
        elif game == len(game_list)-2: str_games += game_list[game] + ', and '
        else: str_games += game_list[game] + ', '

    print('{} all released in {}'.format(str_games, report_year))
    print('{}M total units sold that year'.format(unit_total))


# open our data
filename = start_menu()
fhandle = open(filename, 'r')
data = fhandle.readlines()

# saving headers in list
headers = data[0].strip().split(',')

# saving our data into a list
data_list = []
for line in range(len(data)):
    if line == 0: continue
    if line == 21: break # limiting data to 20 lines atm
    data_list.append(data[line].strip().split(','))
    #print(data[line].strip())

fhandle.close()
# saving header in dictionary with their data type
#header_dict = tag_columns(data_list[0:6])

# menu for data operation
while True:
    print('\nWhat would you like to do with your data?')
    print('(print)(sort by title)(sort by year)(report)(quit)(columns)')
    action = input('>>  ')

    # menu option tree
    if action == 'quit': quit()
    elif action == 'print': print_data()
    elif action == 'sort by title': sort_title(data_list)
    elif action == 'sort by year': sort_year(data_list)
    elif action == 'report':
        while True: # input loop for getting report type
            print('What kind of report?')
            print('(most units)(total units)')
            raction = input('>>  ')

            if raction == 'cancel': break
            elif raction == 'most units':
                report_unit_most(data_list)
                break
            elif raction == 'total units':
                report_unit_total(data_list)
                break
            else: print('\nERROR: entry not recognized\n\n')
    elif action == 'columns': tag_columns(headers, data_list[0:6])
    else: print('\nERROR: entry not recognized\n\n')
