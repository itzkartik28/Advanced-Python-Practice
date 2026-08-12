f=open("write in file.py","r")

data=f.read()

print(data)

f.close()

#the same can be written using with statement like this:
with open("write in file.py") as f:
 print(f.read())