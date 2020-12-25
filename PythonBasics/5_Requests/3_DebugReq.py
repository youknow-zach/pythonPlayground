import requests

def requestURL(baseurl, params = {}):
    # This function accepts a URL path and a params diction as inputs.
    # It calls requests.get() with those inputs,
    # and returns the full URL of the data you want to get.
    req = requests.Request(method = 'GET', url = baseurl, params = params)
    prepped = req.prepare()
    return prepped.url

baseurl = 'https://api.datamuse.com/words'
kval_pairs = {'rel_rhy' : 'cannon'}
print(requestURL(baseurl, kval_pairs))

baseurl = 'https://www.google.com/search'
kval_pairs = {'tbm' : 'isch', 'q' : '"violins and guitars"'}
print(requestURL(baseurl, kval_pairs))
