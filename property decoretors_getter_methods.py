class employee:
    a=1
    @classmethod
    def show(cls):
     print(f"the class attribute of a is{cls.a}")

     @property
     def name(self):
       return f"{self.fname}{self.lname}"

     @name.setter
     def name(self,value):
        self.fname=value.slipt("")[0]
        self.lname=value.slipt("")[1]


e=employee()
e.a=45

e.name="kartik salunkhe"
print(e.name)
e.show()