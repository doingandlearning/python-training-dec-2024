class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person({self.name}, {self.age})"

    def __str__(self):
        return f"A Person aged {self.age} called {self.name}"

    def birthday(self):
        print(f"Happy birthday! You were {self.age}")
        self.age += 1
        print(f"You are now {self.age}.")

    def is_teenager(self):
        return 12 < self.age < 20

    def calculate_pocket_money(self, weeks):
        rate_of_pocket_money = 10
        print(f"Calculating {self.name}'s pocket money!")
        return weeks * rate_of_pocket_money

    def __len__(self):
        return self.age

    def __add__(self, other):
        if type(other) is Person:
            return self.age + other.age
        else:
            raise TypeError("Can't add non Person to Person")




person1 = Person('Ethan', 12)
person2 = Person('Emerald', 10)

print('id(p1):', id(person1))
print('id(p2):', id(person2))
print(person1)
print(person2)
print(person1.name)
print(f"Ethan is a teenager: {person1.is_teenager()}")
person1.birthday()
print(f"Ethan is a teenager: {person1.is_teenager()}")
person2.birthday()

print(person2.calculate_pocket_money(3))
print(len(person1))

print(person1 + person2)

print([person1, person2])
print(f"{person1} this is a person")
print(person1.__dict__)

class Employee(Person):
    pass