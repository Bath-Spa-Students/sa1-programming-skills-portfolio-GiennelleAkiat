def print_message():
    print("beep boop")

def print_message_2():
    Bop = "Bop"
    print_message()
    print(Bop)

print_message_2()

# ===========================

def custom_message(message):
    print(message)

message = input("Type a message you want to print: ")
custom_message(message)


