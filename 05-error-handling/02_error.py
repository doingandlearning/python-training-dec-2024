import traceback

try:
    int(input("Give me a number: "))
    # raise Exception("Something went wrong!")
except ValueError:
    print("You gave something that can't be converted to an integer")
except KeyboardInterrupt as exp:
    print("The program was cancelled by the user. Have a nice day!")
    print(f"Send to log file: KeyboardInterrupt with this message - {exp}")
    # print(f"Logfile: {exp.__context}")
except Exception as e:
    print(e)
    print("This run if something goes wrong!!")
else:
    print("Nothing went wrong!")
finally:
    print("Close connection/tidy subscriptions")

print("This will run even if something goes wrong!")