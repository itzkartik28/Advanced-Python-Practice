class employee:
    company="itc"

    def show(self):
        print(f"the name of the emmployee is{self.name} and the salary is{self.salary}")

class programmer(employee):
    company="itc info"

    def showlanguage(self):
        print(f"the name of the employee is{self.name } and the language of th employee is{self.language}")



a=employee()
b=programmer()

print(b.company,a.company)