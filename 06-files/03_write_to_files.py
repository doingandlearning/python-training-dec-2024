import datetime

# modes
# r = read
# w = write
# a = append

with open("log.txt", mode="a") as file:
    file.write("This is a log file.\n")
    file.write("Working with files is fun!\n")
    file.write(f"{datetime.datetime.now()}\n")