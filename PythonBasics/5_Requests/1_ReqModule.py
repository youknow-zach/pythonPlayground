# The requests module

import requests
import json

# this is using the full URL for a rest API passed into the get method:
#page = requests.get('https://api.datamuse.com/words?rel_rhy=orange')

# here we're using a dict to pass our keywords as parameters
kval_pairs = {'rel_rhy' : 'birdy'}
page = requests.get('https://api.datamuse.com/words', params = kval_pairs)

print(type(page))
#print('HISTORY:\n{}\n'.format(page.history))
#print('HEADERS:\n{}\n'.format(page.headers))
#print('TEXT:\n{}\n'.format(page.text[:150])) # print the first 150 chars
print('URL:\n{}\n'.format(page.url)) # print the url that was fetched
print('------')
x = page.json() # turn page.text into a python object
# ^This is the same as json.loads(page.text)
print(type(x))
print('---first item in the list---')
print(x[0])
print('---the whole list, pretty printed---')
print(json.dumps(x, indent=2)[:300])
