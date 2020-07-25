import requests

# Another noob challenge where a subdirectory to be disallowed from being accesible to web crawling bots is stated in the robots.txt file.

robots = requests.get('http://chall.csivit.com:30231/robots.txt')
print(robots.text)

# Disallow: /fade/to/black

r = requests.get('http://chall.csivit.com:30231/fade/to/black')
print(r.text)