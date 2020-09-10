def display_message():
    print("I am learning about functions in this chapter.")
display_message()

def favourite_book(title):
    print(title + " is my favourite book.")
favourite_book('Aeneid')
print()

def make_shirt(shirt_size, shirt_msg):
    print('The shirt size is ' + shirt_size + ' and the message printed on is ' + '\'' + shirt_msg + '\'' + '.')
make_shirt('Medium', 'Havertz is the GOAT')
make_shirt(shirt_size = 'Large', shirt_msg = 'Werner awaits greatness')
