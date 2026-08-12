class vector:
    def __init__(self,L):
        self.L=L

    def __len__(self):
        return len(self.L)

v1=vector([1,2,3])
print(len(v1))