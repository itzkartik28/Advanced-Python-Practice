f=open("file2.txt")

line=f.readline()
while(line !=""):
    print(line)
    line=f.readline()

f.close()