nsum=0
esum=0
osum=0
for i in range (11):
    nsum+=i
    if(i%2==0):
        esum+=i
    else:
        osum+=i
print("sum of n natural number",nsum)
print("sum of n even number",esum)
print("sum of n odd number",osum)