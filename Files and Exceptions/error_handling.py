def adding(num_one, num_two):
    """Adding two numbers together and catching any errors."""
    try:
        calc = int(num_one) + int(num_two)
    except ValueError:
        if not num_one.isdigit() and not num_two.isdigit():
            print('\nBoth numbers entered are invalid.\n')
        elif not num_one.isdigit():
            print('\nThe first number entered is invalid.\n')
        else:
            print('\nThe second number is invalid.\n')
    else:
        print('\n' + str(calc) + '\n')

while True:
    print('Welcome to Adding. Type \'quit\' at any time to exit.')
    num_one = input('Enter your first number.\n')
    if num_one == 'quit':
        break
    num_two = input('\nEnter your second number.\n')
    if num_two == 'quit':
        break
    adding(num_one, num_two)
