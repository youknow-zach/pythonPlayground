'''
Read in the contents of the file SP500.txt which has monthly data for 2016 and 2017 about the S&P 500
closing prices as well as some other financial indicators, including the “Long Term Interest Rate”, which is
interest rate paid on 10-year U.S. government bonds.

Write a program that computes the average closing price (the second column, labeled SP500) and the
highest long-term interest rate. Both should be computed only for the period from June 2016 through May
2017. Save the results in the variables 'mean_SP' and 'max_interest.'
'''

# Start here
fhandle = open('SP500.txt', 'r')
data = fhandle.readlines()
info = []
headers = []


for line in range(len(data)):
    if line == 0:
        headers.append(data[line].strip().split(','))
        continue
    info.append(data[line].strip().split(','))
    info[line-1][0] = info[line-1][0].split('/')

max_interest_list = [float(amt[5]) for amt in info if
                            (amt[0][2] == '2016' and int(amt[0][0]) >= 6) or
                            (amt[0][2] == '2017' and int(amt[0][0]) <= 5)]
mean_SP_list = [float(amt[1]) for amt in info if
                            (amt[0][2] == '2016' and int(amt[0][0]) >= 6) or
                            (amt[0][2] == '2017' and int(amt[0][0]) <= 5)]

print(headers)

max_interest = 0
for amt in max_interest_list:
    if max_interest < amt: max_interest = amt

print(max_interest_list)
print(mean_SP_list)
print('{} / {} = {}'.format(sum(mean_SP_list), len(mean_SP_list), sum(mean_SP_list)/len(mean_SP_list)))
mean_SP = sum(mean_SP_list)/len(mean_SP_list)

print('\n\n{}\n{}'.format(max_interest, mean_SP))
