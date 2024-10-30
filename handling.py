try:
    f=open('sample.txt','x')
except:
    print('file exists')
with open('sample.txt','r') as f:content =f.read()
lower = 0
upper = 0
for char in content:
    if char.islower():
        lower+1
    elif char.isupper():
        upper+=1
print(f"number of lowercase letter:{lower}")

print(f"number of uppercase letter:{upper}")
