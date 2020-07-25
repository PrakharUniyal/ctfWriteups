import requests
import base64
from urllib.parse import unquote

# This has obviously got something to do with the cookies.

page = requests.get('http://chall.csivit.com:30243')
print(page.text)

cookies = dict(page.cookies)
print(cookies)
# Looks like b64 encoded.

print(base64.decodestring(unquote(cookies['flavour']).encode()))

# So we need to change the flavour cookie to chocolate instead of strawberry.
cookies['flavour'] = str(base64.encodestring('chocolate'.encode()))[2:-3]

# Send request with modified cookie:
r = requests.get('http://chall.csivit.com:30243',cookies=cookies)
print(r.text)