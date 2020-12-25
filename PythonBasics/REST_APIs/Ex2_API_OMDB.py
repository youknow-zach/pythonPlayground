import json
import requests

# this is using the full URL for a rest API passed into the get method:
#page = requests.get('https://api.datamuse.com/words?rel_rhy=orange')

# here we're using a dict to pass our keywords as parameters
omdb_parms = {}
omdb_parms['s'] = 'Starship Troopers'
omdb_parms['apikey'] = '5831670f'
omdb_parms['type'] = 'movie'
omdb_parms['r'] = 'json'

page = requests.get('http://www.omdbapi.com/', params = omdb_parms)

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

quit()

# This is all extra stuff messing with storing the returned info
moviedata = {}

for entry in range(len(data['Search'])):
    for k, v in data['Search'][entry].items():
        key = '{}_{}'.format(str(entry), k)
        moviedata[key] = v
        #print(moviedata[key])

for k, v in moviedata.items():
    print('{} entry is: {}'.format(k, v))
