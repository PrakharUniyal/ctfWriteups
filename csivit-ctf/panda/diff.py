import os

# diff utility on terminal could have been used however I have never been able to use it correctly with binary data.
# So we will do a hexdump of files and implement a script that gives a neat diff of the two files. Hexdump strips the non-ASCII data from the textual representation which makes it easy to do comparisons.

os.system('xxd panda.jpg > 0.txt && xxd panda1.jpg > 1.txt')
os.system('rm *.jpg')

with open('0.txt','r') as file1:
    data1 = file1.read().split('\n')
with open('1.txt','r') as file2:
    data2 = file2.read().split('\n')

os.system('rm *.txt')

if(len(data1)!=len(data2)):
    print('Length not equal.')
else:
    s1,s2 = "",""
    for i in range(len(data1)):
        x,y = data1[i][51:],data2[i][51:]
        if(x!=y):
            for j in range(len(x)):
                if(x[j]!=y[j]):
                    s1+=x[j]
                    s2+=y[j]
    print(s1) if s1.find('csi')>-1 else print(s2)
