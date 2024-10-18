# 
# s={1,2,3,4,5}

# s=set()
# s.add(1)
# s.update({2,3,4,5})
# s.discard(9)
# # s.remove(6)
# # s.pop()
# print(s)

# s={1,2,3,4,5}
# s1={1,2,3}
# print(s.intersection(s1))
# print(s.isdisjoint(s1))
# print(s.issubset(s1))
# print(s.issuperset(s1))
# print(s.union(s1))
# print(s.difference(s1))

s={1,2,3,4,5}
s1={1,2,3,6}
s2=s.copy( )
s.difference_update(s1)
# # s.intersection_update(s1)
# s.symmetric_difference_update(s1)
print(s)