class Person:

    no_of_persons = 0

    def __init__(self,name,age):
        self.name=name
        self.age=age
        Person.add_people()

    def show(self):
        print(f"I am {self.name} and I am {self.age}years old")


    @classmethod
    def number_of_people(cls):
        return cls.no_of_persons
    
    @classmethod
    def add_people(cls):
        cls.no_of_persons += 1


p1 = Person("varun",35)
p1.show()
print(p1.no_of_persons)

p2 = Person("arya",33)
p2.show()
print(p2.no_of_persons)