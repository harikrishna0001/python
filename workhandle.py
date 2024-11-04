try:
    f=open('line.txt','x')
except:
    print('file exists')

f=open('line.txt','r')

b=f.readlines()
print(b)
words = 0
f=open('line.txt','r')
data = f.read()
lines = data.split()
words += len(lines)
print(words)
f=open('line.txt','r')
lower = 0
upper = 0
for i in f:
    for j in i:
        if j.islower():
            lower+=1
        elif j.isupper():
            upper+=1
print("number of lowercase letter",lower)

print("number of uppercase letter",upper)