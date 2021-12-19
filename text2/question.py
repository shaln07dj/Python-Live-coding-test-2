from _typeshed import Self


class Calcuator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def add(self):
        self.sum=self.num1+self.num2
        print(self.sum)

    def substract(self):
        self.sub=self.num1-self.num2
        print(self.sub)

    def multiply(self):
        self.mul=self.num1*self.num2
        print(self.mul)
    
    def divide(self):
        self.div=self.num1/self.num2
        print(self.div)

obj=Calcuator(10,5)
obj.add()
obj.substract()
obj.multiply()
obj.divide()