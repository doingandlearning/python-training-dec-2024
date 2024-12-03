if True:
    print("It was true!")

location = "edinburgh"

if location.islower():
    print("Don't forget to user capital letters at the start!")
    print(location.title())
else:
    print(location)

command = "read"
print("About to hit the if statement")

if command == "delete":
    print("Delete table")
elif command == "create":
    print("Create table")
elif command == "modify":
    print("Modify table")
else:
    print("We do not understand that command.")

print("Just finished the if statement")

# cyclomatic complexity

is_raining = True
temperature = 10
if is_raining:
    if temperature < 0:
        print("Be careful! It might snow")
    else:
        print("Don't forget your umbrella!")
else:
    print("Lovely day, isn't it!")


if is_raining and temperature < 0:
    print("Be careful! It might snow!")


if is_raining or temperature < 0:
    print("Stay indoors.")







