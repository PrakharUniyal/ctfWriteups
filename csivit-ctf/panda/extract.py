import os
import zipfile
# pip3 install tqdm
from tqdm import tqdm

zip_file = "panda.zip"

# The given zip file is encoded with a pin (of 4 to 6 digits).
# Create a wordlist with all possible pin combinations.
wordlist = 'wordlist.txt'
with open(wordlist,"w") as wl:
    wl.write('\n'.join(
        [('0'*(4-len(str(i))))+str(i) for i in range(100000)]+
        [('0'*(5-len(str(i))))+str(i) for i in range(100000)]+
        [('0'*(6-len(str(i))))+str(i) for i in range(100000)]
        ))

# initialize the Zip File object
zip_file = zipfile.ZipFile(zip_file)
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
            break

os.system('rm wordlist.txt')