from functools import reduce
# l=[1,2,3,4]
# res=reduce(lambda x,y:x+y,l)
# print(res)

# 10

def hm(x,y):
    return x+y
l=[1,2,3,4]
res=reduce(hm,l)
print(res)

10