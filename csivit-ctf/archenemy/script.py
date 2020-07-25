import os
import zipfile
# pip3 install tqdm
from tqdm import tqdm

# Looking at the strings of the given image we can figure out that steghide has been used.
# Trying a blank password yields the hidden zip file.
os.system('steghide extract -sf arched.jpg -p ""')

# However the zip file is password protected. Looking at the strings of the zip file we see the string 'We will, we will, ROCKYOU!PK' appended at the end.
# This must be a hint towards the famous rockyou.txt wordlist to brute force password for zip file.
# (https://github.com/praetorian-code/Hob0Rules/blob/master/wordlists/rockyou.txt.gz)
wordlist = '/mnt/d/Codes/rockyou.txt'

# initialize the Zip File object
zip_file = zipfile.ZipFile('flag.zip')

# count the number of words in this wordlist
n_words = len(list(open(wordlist, "rb")))

# Brute force the wordlist on zip file
with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist, total=n_words, unit="word"):
        try:
            zip_file.extractall(pwd=word.strip())
        except:
            continue
        else:
            print("Password found:", word.decode().strip())
            os.system('rm flag.zip')
            break

# Zip file yields an image with the flag:
# csictf{1_h0pe_y0u_don't_s33_m3_here}