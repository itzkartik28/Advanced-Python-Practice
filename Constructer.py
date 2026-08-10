class employee:
    name="kartik" 
    salary=19999999999


    def __init__(self,name,salary,language):
        self.name=name
        self.salary=salary
        self.language=language
        print("i am creating an object")
    
    def getinfo(self):
        print(f"the language is{self.name} and the salary is{self.salary}")




kartik=employee("kartik",2000000000000000,"java")
print(kartik.name,kartik.salary,kartik.language)
kartik.salary=2000000000000000
#kartik.getinfo()
employee.getinfo(kartik)