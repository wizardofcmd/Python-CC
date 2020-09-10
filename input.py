car = input("What sort of car would you like to rent? ")
print("Let me see if I can find you a " + car + ".")

seated = input("How many guests are you having for dinner? ")
if int(seated) > 8:
    print("You will have to wait a bit longer for a table.")
else:
    print("Follow me to be seated.")

multiple = input("Enter any number. ")
if int(multiple) % 10 == 0:
    print("This number is a multiple of 10.")
else:
    print("This number is not a multiple of 10.")
