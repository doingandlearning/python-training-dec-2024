def square(n):
    return n * n


square = lambda n: n * n

add = lambda a,b: a + b

numbers = [1,2,3,4,5,6]

print(list(map(lambda n: n * n, numbers)))

square_list = []
for number in numbers:
    square_list.append(square(number))
print(square_list)

# List comprehension
print([square(number) for number in numbers])


def cube(n):
    return n * n * n