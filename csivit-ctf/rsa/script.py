import os

with open('enc.txt','r') as f:
    data = [i.split(' = ')[1] for i in f.read().split('\n')]

n,e,c = data[0],data[1],data[2]

# It is evident that n is not very big. Hence the public key is weak. We can easily factorize n to get the totient function calculate the private key from it.
# I have used the RsaCtfTool(https://github.com/Ganapati/RsaCtfTool) for this challenge.

path_to_script = './RsaCtfTool/'
os.system('python3 '+path_to_script+'RsaCtfTool.py -n '+n+' -e '+e+' --uncipher '+c+' --attack factordb')