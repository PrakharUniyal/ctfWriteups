import requests

# This is one of those cliché challenges where flag is written as a comment in a static file like style.css

r = requests.get('http://chall.csivit.com:30203/static/style.css')
print(r.text)