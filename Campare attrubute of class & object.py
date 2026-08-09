class demo:
    a=4

o=demo()
print(o.a)#print 4 beasuse the object attribute was not present
o.a=0  # object attribute creted
print(o.a) #it print object attribute value
print(demo.a) # but not change the class attribute value