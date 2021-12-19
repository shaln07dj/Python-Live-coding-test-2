class Point:
    def __int__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def sum(self):
        sumPoint=[(self.x**2)+(self.y**2)+(self.z**2)]
        return({sumPoint})


obj=Point(1,3,5)
print(obj,sum())
