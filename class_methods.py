class Person:
    total_persons = 0  # Class-level attribute to store the total number of persons
    names = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.total_persons += 1  # Increment the total_persons count when a new person is created
        Person.names.append(self.name)

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

    @classmethod
    def get_total_persons(cls):
        return cls.total_persons
    
    @classmethod
    def names_list(cls):
        return cls.names

# Creating instances of Person class
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Calling class method to get the total number of persons
total_persons = Person.get_total_persons()
print(f"Total persons: {total_persons}")  # Output: Total persons: 2

print(Person.names_list())

