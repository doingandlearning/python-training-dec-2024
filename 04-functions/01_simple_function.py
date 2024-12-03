def print_msg():
    """
    A function to print message
    :return:
    """
    print("Hello!")

print_msg()

def print_msg(message, speaker):
    print(f"{speaker}: {message}")

print_msg("Hello, how are you?", "Alex")
print_msg("I am fine thanks.", "Douglas")