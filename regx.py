# import re

# a="welcome to all"
# s=re.split("o",a)
# print(s)

# substitution


# import re

# a="welcome to all"
# s=re.sub("to"," ",a)
# print(s)

# findall

# import re

# a="welcome all to the world of race"
# f=re.findall('\s',a)
# print(f)

# search

# import re

# a="welcome all to the world of race"
# f=re.search('o',a)
# print(f)

# import re

# a="welcome all to the world of race"
# print(re.search("t.*",a))


# import re

# a="welcome all to the world of race"
# print(re.search("w.+",a))



# to print 0 and 1 value

# import re 

# a="welcome"
# print(re.search("w.?",a))

# to chck and print first lower letter


# import re 

# a="welcome"
# print(re.search('[a-z]',a))

#  to chck and print first capital letter


# import re 

# a="welcome"
# print(re.search('[A-Z]',a))

#  to chck and print number


# import re 

# a="welcome"
# print(re.search('[1-9]',a))

#  to chck and print first any type of letters,number,special charactres,etcs


# import re 

# a="3welcome"
# print(re.search('[a-zA-Z0-9]',a))


#  to chck and print three of them where in  


# import re 

# a="wL0"
# print(re.search("[a-z][A-Z][0-9]",a))

#  to chck and print how many lettrs are there


# import re 

# a="welcome"
# print(re.search('[a-z]',a))


#  to chck the password


import re 

a=input("enter your password to check its strenght :")
res=re.search('[A-Z].[7]',a)
if res:
    print("password is strong")
else:
    print("password is weak")