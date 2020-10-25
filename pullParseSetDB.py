# Pull from URL: http://py4e-data.dr-chuck.net/comments_917124.json
# break out the JSON information
# link up users with their ID numbers
# many-to-many database linking users with the letters in their names

import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    url = input('Enter URL or quit: ')
    if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_917124.json'
    elif url == 'quit': quit()

    print('Retrieving', url)
    try:
        uh = urllib.request.urlopen(url, context=ctx)
        data = uh.read().decode()
    except:
        print('==== Not a valid URL. Try again ====')
        continue
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js:
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))
