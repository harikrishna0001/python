try:
    f=open('reverse.txt','x')
except:
    print('file exists')
f=open('reverse.txt','w')
f.write("welcome"[::-1])
print(f)

