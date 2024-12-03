def print_msg():
    """
    A function to print message
    :return:
    """
    print("Hello!")

print_msg()

def print_msg(message, speaker="Alex", volume="loud"):
    print(f"{speaker} (at {volume} volume): {message}")

print_msg( volume="quiet", message="How are you?")
print_msg("I am fine thanks.", "Douglas", "quiet")
print_msg("🔑😇")