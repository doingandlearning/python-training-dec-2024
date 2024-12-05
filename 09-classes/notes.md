# Plan for Session
- Everything is an Object
- Class Terminology
- Defining user-defined classes
- Instantiating Objects from Classes
- Printing Objects
- Be careful with assignment
- Class Comments
- Defining behaviour
- Deleting an object

---

## Everything in Python is an Object
- Objects are examples/instances of Classes.
- Classes act as templates for objects, defining the data/behavior of the object.
- Example: Class `Person`.
- Objects (or instances) of a class hold actual data values & are used to execute behavior.
- There can be many objects for a given class (e.g., class `Person` may have instances John, Denise, Phoebe, and Gryff).

### Example:
```python
print(type(4))         # <class 'int'>
print(type(5.6))       # <class 'float'>
print(type(True))      # <class 'bool'>
print(type('Ewan'))    # <class 'str'>
print(type([1, 2, 3])) # <class 'list'>
```

---

## Class Terminology
- **Class**: A template defining data and behavior that operates on that data.
- **Instance or Object**: 
  - All instances of a class possess the same data fields/attributes but contain their own data values.
  - Each instance of a class responds to the same set of requests.
- **Attribute / Field / Instance Variable**: The data held by an object is represented by its attributes.
- **Method**: A function executed within an object.
- **Message**: A request for some behavior/data from an object.

---

## Can Create User-Defined Classes
- A class definition has the format:

### Example:
```python
class NameOfClass:
    def __init__(self):
        # methods

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```
- The class name follows Camel Case conventions with no spaces (or `_`).
- Defines two attributes: `name` and `age`.
- Also defines a special method called `__init__` (object initializer aka constructor).

---

## Creating Objects from Class Person
- Objects are created using the name of the class and passing in the values for parameters of the initializer method.

### Example:
```python
p1 = Person('John', 36)
p2 = Person('Phoebe', 21)

print('id(p1):', id(p1))
print('id(p2):', id(p2))
```
- Each object/instance is unique and has its own unique ID number.

---

## Printing Objects
- Can print out an object.
- By default, it prints the name and indicative address in memory, which makes it hard to work out which object is which.
- Can print attributes directly.
- Can override the default behavior using `__repr__()` (another special method, also see `__str__`).

### Example:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return self.name + ' is ' + str(self.age)

print(p1)
print(p2)
```

---

## Be Careful with Assignment
- Assignment copies the address of an object.

### Example:
```python
p1 = Person('John', 36)
p2 = Person('Phoebe', 21)

px = p1

print(p1)
print(px)

print('id(p1):', id(p1))
print('id(px):', id(px))
```
- May not be obvious when printed, but IDs make it clear.

---

## Class Comment
- A docstring for a class is considered good practice.
- Typically provides information on the purpose of the class.
- Often gives guidance on usage.

### Example:
```python
class Person:
    """An example class to hold a person's name and age"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return self.name + ' is ' + str(self.age)
```

---

## Adding Behaviour
- Add some behavior.
- The first parameter to the method is always a reference to the object, called `self` by convention.
- Method names follow variable naming conventions.

### Example:
```python
class Person:
    """An example class to hold a person's name and age"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return self.name + ' is ' + str(self.age)

    def birthday(self):
        print('Happy birthday! You were', self.age)
        self.age += 1
        print('You are now', self.age)

p3 = Person('Adam', 21)
print(p3)
p3.birthday()
print(p3)
```

---

## Adding Behaviour with Parameters and Return Values
- Methods can have parameters and/or return values.

### Example:
```python
class Person:
    """An example class to hold a person's name and age"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def calculate_pay(self, hours_worked):
        rate_of_pay = 7.50
        if self.age >= 21:
            rate_of_pay += 2.50
        return hours_worked * rate_of_pay

    def is_teenager(self):
        return self.age < 20

pay = p2.calculate_pay(40)
print(f'Pay {p2.name}: {pay}')

pay = p3.calculate_pay(40)
print(f'Pay {p3.name}: {pay}')

print(f'p2.is_teenager: {p2.is_teenager()}')
```

---

## Deleting Objects
- Objects can be deleted either because:
  - The variable referencing the object goes out of scope.
  - The variable is set to `None`.
  - The `del` keyword is applied to the variable.

### Example:
```python
p1 = Person('John', 36)
print(p1)
del p1
```
- After the `del` statement, the object held by `p1` will no longer be available, and any attempt to reference it may generate an error.

---

## Questions?

?