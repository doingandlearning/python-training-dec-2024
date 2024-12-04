try:
    with open("file.txt") as file:
        contents = file.readlines()
        for line in contents:
            print(line.strip())
except FileNotFoundError:
    print("File not there!")