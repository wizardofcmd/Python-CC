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

responses = {}
active = True

while active:
    name = input('What is your name? ')
    response = input('What country would you like to visit the most? ')
    responses[name] = response

    repeat = input('Would you like another person to take part in the poll? Please write \'yes\' or \'no\'. ')
    if repeat.lower() == 'no':
        break

for person in responses:
    country = responses[person]
    print(person + ' would like to visit ' + country + '.')

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
