class Student:
    def __init__(self):
        self.name=""
        self.phy=0
        self.chem=0
        self.bio=0

    def totalObtained(self,name,phy,chem,bio):
        self.name=name
        self.phy=phy
        self.chem=chem
        self.bio=bio
        self.total= self.phy+self.chem+ self.bio
        return(self.total)


if __name__=="__main__":
    obj=Student()
    name=input("Enter the Name")
    phy=int(input("Enter the phy"))
    chem=int(input("Enter the chem"))
    bio=int(input("Enter the bio"))
    print( obj.totalObtained(name,phy,chem,bio))

    