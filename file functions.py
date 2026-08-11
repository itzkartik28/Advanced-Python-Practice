f=open("file for measure.txt","r")

#this is for multiple lines
#lines=f.readlines()
#print(lines,type(lines))

#this is for indiual line

#line1=f.readline()
#print(line1,type(line1))

#line2=f.readline()
#print(line2,type(line2))

#line3=f.readline()
#print(line3,type(line3))


line=f.readline()
while(line !=""):
    print(line)
    line=f.readline()

f.close()