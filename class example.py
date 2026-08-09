from random import randint

class train:

    def __init__(self,trainno):
        self.trainno=trainno


    def book(self,fromm,to):
        print(f"ticket is booked in {self.trainno} from {fromm} to {to}")

    def status(self):
        print(f"train no {self.trainno} is running on time")

    def ticket(self,fromm,to):
        print(f" ticket fare in train no is {self.trainno} from {fromm} to {to} price is {randint(222,555)}")



t=train(128999)
t.book("mumbai","pune")
t.status()
t.ticket("mumbai","pune")