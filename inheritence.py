class Pet:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(f"I am {self.name} and I am {self.age} years old")
    
    def speak(self):
        print("I dont know what to say")

class Dog(Pet):

    def speak(self):
        print("Bark!")

class Cat(Pet):
    def speak(self):
        print("Meow!")

class Fish(Pet):
    pass


p1 = Pet("Manu",34)
d1 = Dog("Varun", 35)
d1.speak()
c1 = Cat("Arya", 33)
c1.speak()
f1 = Fish("Nemo", 3)
f1.speak()