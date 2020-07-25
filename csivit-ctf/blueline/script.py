import numpy as np

# Using the given java classfile we found:
key_string = "gybnqkurp"

# this key_string is converted into a square matrix with values corresponding to A0Z25 encoding row-wise for further use:
key = [[6,24,1],[13,16,10],[20,17,15]]

# By some basic analysis it is evident that segments of key consisting of 3 letters will have the same encryption irrespective of their positiion.
# As only lowercase alphabets are being used, it will be convenient to generate a hash table for all possible segments using brute force.

alphabets = [chr(ord('a')+i) for i in range(26)]

vals = []
for a1 in alphabets:
    for a2 in alphabets:
        for a3 in alphabets:
            vals.append(a1+a2+a3)

codes = {}
for val in vals:
    segment = [[ord(val[i])-97] for i in range(3)]
    encoded_segment = np.matmul(key,segment)

    for i in range(len(encoded_segment)):
        for j in range(len(encoded_segment[i])):
            encoded_segment[i][j]%=26

    enc_val = ''.join([chr(i[0]+97) for i in encoded_segment])
    codes[enc_val] = val

# Read encoded flag:
with open('theclimb.txt','r') as key:
    text = key.read().split(' = ')[1]

# Decode:
for i in range(0,len(text),3):
    print(codes[text[i:i+3]],end='')
print()

# Output: hillhaveeyesxx (xx are for padding)