try:
    f=open('sample.txt','x')
except:
    print('file exists')
    
# f=open('sample.txt','w')
# f.write("welcome ")
# f=open('sample.txt','a')
# f.write("buddies")

f=open('sample.txt','r')
# a=f.read(3)
# b=f.read()
c=f.readline(3)
d=f.readlines()
# print(a)
# print(b)
print(c)
print(d)


