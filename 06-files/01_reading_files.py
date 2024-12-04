file = open("file.txt")

print(file)
contents = file.read()
print(contents)

file.seek(0)
contents = file.readlines()

for line in contents:
    print(line.strip())

file.seek(0)

print(file.readline().strip())
print(file.readline().strip())
print(file.readline().strip())
print(file.readline().strip())
print(file.readline().strip())
print(file.readline().strip())
print(file.readline().strip())
print(file.readline().strip())









file.close()