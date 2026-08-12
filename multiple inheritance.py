class employee:
    company="itc"
    name="defalt"
    

    def show(self):
        print(f"the name of the emmployee is{self.name} and the salary is{self.company}")


class coder:
    langage="python"
    def printlanguage(self):
        print(f"the lanuage is {self.langage}")

class programmer(employee,coder):
    company="itc info"

    def showlanguage(self):
        print(f"the name of the employee is{self.name } and the language of th employee is{self.langage}")



a=employee()
b=programmer()
c=coder()
print(b.company,a.company)
b.show()
b.printlanguage()
b.showlanguage()