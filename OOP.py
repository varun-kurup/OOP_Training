# Defining a class
class Box:

    def __init__(self,name):
        self.name = name

    def get_name(self):
        return self.name

    def add_one(self,x):
        return(x+1)
    
    def sound(self):
        return("Bow Bow!")
    
#inst = Box()

#print(inst.add_one(9))

i1 = Box("Black")
print(i1.get_name())

i2 = Box("Orange")
print(i2.get_name())

