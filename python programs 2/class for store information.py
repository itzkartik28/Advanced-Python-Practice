class programmer:
    company="microsoft"

    def __init__(self,name,salary,city):
        self.name=name
        self.salary=salary
        self.city=city


k=programmer("kartik",2000000000,"mumbai")
print(k.name,k.salary,k.city,k.company)
p=programmer("pavan",300000000,"mumbai")
print(p.name,p.salary,p.city)