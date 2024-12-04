counter = 0

def add_one_to_variable():
    global counter
    print(counter)
    counter = counter + 1

print(counter)
add_one_to_variable()
print(counter)