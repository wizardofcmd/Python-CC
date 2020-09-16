usernames = ['admin', 'john', 'barry', 'blue', 'silver']
for name in usernames:
    if name == 'admin':
        print("Hello " + name + " would you like to see a status report today?")
    else:
        print("Hello " + name + ", welcome.")
print()

for name in usernames:
    usernames.remove(name)
if usernames:
    print("We need to find some users!\n")

current_users = ['barry', 'blue', 'SILVER', 'hau', 'may']
new_users = ['barry', 'red', 'silver', 'ruby', 'diamond']

for name in current_users:
    name = name.lower()
    if name in new_users:
        print('This name is taken. Please choose a new name.')
    else:
        print('This name may be used.')
print()

ordinals = [value for value in range(1,10)]
for number in ordinals:
    if number == 1:
        print(str(number) + "st")
    elif number == 2:
        print(str(number) + "nd")
    elif number == 3:
        print(str(number) + "rd")
    else:
        print(str(number) + "th")
