class employee:
    a=1

class programmer(employee):
    b=2

class manager(programmer):
    c=3

o=employee()
print(o.a)
#does not print be show error
o=programmer()
print(o.b,o.a)

o=manager()
print(o.a,o.b,o.c)