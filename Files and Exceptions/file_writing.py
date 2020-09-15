filename = 'guest.txt'
user = input('Enter your name please. ')

with open(filename, 'w') as file_object:
    file_object.write(user)

filename = 'guest_book.txt'
active = True
while active:
    name = input('Welcome to Appleville. Please tell us your name so that we '
    + 'may record your visit.\nEnter \"quit\" at any time to exit.\n')
    if name.lower() == 'quit':
        active = False
    elif name.lower() == 'reset':
        with open(filename, 'w') as file_object:
            file_object.close()
    else:
        print("\nEntering your name into the guest book. Enjoy your stay!\n")
        with open(filename, 'a') as file_object:
            file_object.write(name + "\n")
