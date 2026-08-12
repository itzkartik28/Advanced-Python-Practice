class employee:
    a=1
    def __init__(self):
        print(" employee class constracter")

class programmer(employee):
    b=2
    def __init__(self):
            print("programer class constracter")

class manager(programmer):
    c=3
    
    def __init__(self):
            super().__init__()
            print(" manager class constracter")

#o=employee()
#print(o.a)
#does not print be show error

#o=programmer()
#print(o.b,o.a)

o=manager()
print(o.a,o.b,o.c)