with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents + "\n")

filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
    print()

with open(filename) as file_object:
    lines = file_object.readlines()

    for line in lines:
        print(line.rstrip())
    print()

filename = 'pi_milli.txt'
with open(filename) as file_object:
    pi_string = ''
    lines = file_object.readlines()
    for line in lines:
        pi_string += line.rstrip()

    birthday = input('Enter your birthday in dd/mm/yy format. ')
    if birthday in pi_string:
        print('Your birthday appears in pi! Congratulations!')
    else:
        print('Sorry! Your birthday doesn\'t appear in pi.')
