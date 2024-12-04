def print_division_result():
    try:
        num1 = int(input("Give me the first number: "))
        num2 = int(input("Give me the second number: "))
        result = num1 / num2
        print(f"Result: {result}")
        raise IOError("This is a new error")
    except ValueError:
        print("You tried to give something that couldn't be converted to an integer")
        print_division_result()
    except ZeroDivisionError:
        print("Oops! You can't divide by zero!")
        print_division_result()

def get_valid_input():
    try:
        num1 = int(input("Give me the first number: "))
        num2 = int(input("Give me the second number: "))
        return num1, num2
    except ValueError:
        get_valid_input()

try:
    num1, num2 = get_valid_input()

    try:
        result = num1/num2
        print(result)
    except ZeroDivisionError:
        print("You tried to divide by zero")

except:
    print("Something unexpected went wrong!")