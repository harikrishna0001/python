import os
foldername=input("enter the name of the folder:")
os.mkdir(foldername)
filename=input("enter the filename :")
f=open(foldername+'/'+filename,'w')
