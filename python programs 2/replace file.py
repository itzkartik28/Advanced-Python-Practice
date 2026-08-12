word="donkey"

with open("file3.txt","r") as f:
    content=f.read()

contentnew =content.replace(word,"######")

with open("file3.txt","w") as f:
    f.write(contentnew)