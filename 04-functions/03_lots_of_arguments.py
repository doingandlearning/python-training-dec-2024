def add(a,b):
    return a + b

print(add(1,4))

def add_three(a,b,c):
    return a + b + c

print(add_three(1,2,3))

def add(name, *numbers):
    total = 0
    for number in numbers:
        total += number
    return f"{name}'s total is {total}"

print(add("Kevin",1,4))
print(add("Gordon",1,2,3))