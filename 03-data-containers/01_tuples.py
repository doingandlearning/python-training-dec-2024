empty_tuple = ()

print(empty_tuple)
print(type(empty_tuple))

#         0  1  2  3  4  5  6
tuple1 = (1, 3, 5, 7, 1, 1, 1)

print(tuple1.count(1))  # how many times does 1 occur in my tuple
print(tuple1.index(1))  # at what index does the value 1 occur first
print(tuple1[3]) # give me the value at index 3
print(tuple1[1:4])  # give me the values from 1 to 4
print(tuple1[:3])  # give me everything upto but not including the value at index 3
print(tuple1[2:]) # give me everything from index 2 to the end
print(tuple1[1:5:2])
print("Hello Everything"[::-1])
print(tuple1[-1])

print(f"There are {len(tuple1)} elements in this tuple")

if 4 in tuple1:
    print("Yes, it is!")
else:
    print("It was not!")


for num in tuple1:
    print(num)