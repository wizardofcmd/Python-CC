import json

def new_number():
    num = input('Please enter your favourite number.\n')
    filename = 'number.json'
    with open(filename, 'w') as file_object:
        json.dump(num, file_object)

def get_number():
    filename = 'number.json'
    try:
        with open(filename) as file_object:
            num = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return num

def enter_num():
    print('Hello user, let me check if you have given your favourite number.\n')
    num = get_number()
    if num:
        print('Your favourite number is ' + num + '!')
    else:
        new_number()
        print('\nWe have stored your number. Come back to verify that we did!')

enter_num()
