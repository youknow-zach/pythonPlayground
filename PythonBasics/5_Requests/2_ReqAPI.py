# The requests module
import requests
import json

# this is using the full URL for a rest API passed into the get method:
#page = requests.get('https://api.datamuse.com/words?rel_rhy=orange')
def getRhyme(w):
# here we're using a dict to pass our keywords as parameters
    req = w
    kval_pairs = {'rel_rhy' : req}
    page = requests.get('https://api.datamuse.com/words', params = kval_pairs)

    #print(page.url)
    x = page.json() # turn page.text into a python object
    results = [dict['word'] for dict in x]
    if len(results) > 3: return results[:3]
    else: return results

print(getRhyme('man'))
print(getRhyme('surge'))
print(getRhyme('tomato'))
