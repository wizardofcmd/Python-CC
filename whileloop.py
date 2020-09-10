finished_sandwiches = []
sandwich_orders = ['Bacon, Lettuce and Tomato', 'Pastrami', 'Chicken & Stuffing', 'Pastrami', 'Egg Mayo', 'Pulled Pork', 'Pastrami']

print(sandwich_orders)
print("There is no more pastrami left. Removing all pastrami sandwich orders.")
while sandwich_orders:
    made = sandwich_orders.pop()
    if made == 'Pastrami':
        continue
    finished_sandwiches.append(made)
    print(made + " sandwich has been made.")
print()

'''
active = True
while active:
    topping = input("Hello customer. What topping would you like on your pizza? ")
    if topping == 'quit':
        break
    print(topping + " will be added to your pizza.")
'''

'''
while True:
    age = input("Welcome to the cinema. What age are you? ")
    if age == 'quit':
        break
    elif not age.isdigit():
        print("Run the program again and enter a valid input :)")
        break
    elif int(age) < 3:
        print("The ticket is free.")
    elif int(age) >= 3 and int(age) <= 12:
        print("The ticket is $10.")
    elif int(age) > 12:
        print("The ticket is $15.")
'''
