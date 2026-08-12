class calculeter:

    def __init__(self,n):
        self.n=n


    def square(self):
        print(F"the square is{self.n*self.n}")

    def cube(self):
           print(F"the square is{self.n*self.n*self.n}")


    def squareroot(self):
                   print(F"the square is{self.n**1/2}")

    @staticmethod
    def greet():
           print("hello there!!")




a=calculeter(4)
a.greet()
a.square()
a.cube()
a.squareroot()