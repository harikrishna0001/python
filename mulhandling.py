try:
    f=open('multiple.txt','x')
except:
    print('file exists')

limit=int(input("enter the limit :"))
f=open('multiple.txt','w')
for i in range(1,11):
    for j in range(1,limit+1):
        f.write(str(i)+'*'+str(j)+'='+str(i*j)+'\t')
        f.write('\n')