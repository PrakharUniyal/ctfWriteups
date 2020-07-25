import requests

# Get request to page
page = requests.get("http://chall.csivit.com:30281")
print(page.text)

# There is obfuscated javascript code that is being used to validate the password.
# Deobfuscate and retrieve the password from it.

# Do a post request with the found password
data = {"password": "5W$Fbb=+nBE*pg4t^7M"}
r = requests.post("http://chall.csivit.com:30281", data=data)

print(r.text)