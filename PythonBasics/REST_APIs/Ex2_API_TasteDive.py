import json
import requests

# this is using the full URL for a rest API passed into the get method:
#page = requests.get('https://api.datamuse.com/words?rel_rhy=orange')

# here we're using a dict to pass our keywords as parameters
td_parms = {}
td_parms['q'] = 'Gremlins'
td_parms['k'] = '395289-Python3-5E7HNN7G'
td_parms['info'] = '1'
td_parms['limit'] = '5'

page = requests.get('https://tastedive.com/api/similar', params = td_parms)

print(type(page))
#print('HISTORY:\n{}\n'.format(page.history))
#print('HEADERS:\n{}\n'.format(page.headers))
#print('TEXT:\n{}\n'.format(page.text[:150])) # print the first 150 chars
print('URL:\n{}\n'.format(page.url)) # print the url that was fetched
print('------')
data = page.json() # turn page.text into a python object
# ^This is the same as json.loads(page.text)
print(type(data))
print('---the whole list, pretty printed---')
print(json.dumps(data, indent=2))
