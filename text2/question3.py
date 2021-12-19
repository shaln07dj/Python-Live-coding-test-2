class Shape:
    def __init__(self):
        self.ar=0
        
    def area(self):
        print(self.ar)

class Square(Shape):
    def __init__(self,length):
        super().__init__()
        self.length=length


    def area(self):
        self.ar=self.length**2
        print(self.ar)

obj1=Shape()
obj2=Square(7)
obj2.area()      
