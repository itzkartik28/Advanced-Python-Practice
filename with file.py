f=open("file2.txt")
print(f.read())
f.close()

#the same can be written using with statement like this:
with open("file2.txt") as f:
    print(f.read())

    #you dont have close the file