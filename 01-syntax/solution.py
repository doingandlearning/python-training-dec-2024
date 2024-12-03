import sys

print(sys.argv)

# sys.argv[1]
# sys.argv[2]
if len(sys.argv) > 1:
    first_number = int(sys.argv[1])
else:
    first_number = int(input("What is the first number? "))

if len(sys.argv) > 2:
    second_number = int(sys.argv[2])
else:
    second_number = int(input("What is the second number? "))


sum = first_number + second_number
difference = first_number - second_number
product = first_number * second_number
quotient = first_number / second_number

print(f"The sum is { first_number + second_number}")
print(f"The difference is {first_number - second_number}")
print(f"The product is {product}")
print(f"The quotient is {quotient}")

print("The sum is " + str(sum))
print("""

It respects new line characters!

""")
