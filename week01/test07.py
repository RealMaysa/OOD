import math

class Spherical:
    
    def __init__(self,r):
        self.radius=r
        self.findVolume()
        self.findArea()

    def changeR(self,Radius):
        self.radius=Radius
        self.findVolume()
        self.findArea()

    def findVolume(self):
        return (4/3) * math.pi * (self.radius *self.radius * self.radius)
        
        

    def findArea(self):
        return 4 * math.pi * (self.radius*self.radius)
        
        

    def __str__(self):
        
        return f'Radius ={self.radius} Volumn = {self.findVolume()} Area = {self.findArea()}'


r1,r2 = input("Enter R : ").split()
R1 = Spherical(int(r1))
print(type(R1))
print(dir(R1))
print(R1)
R1.changeR(int(r2))
print(R1)