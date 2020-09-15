def print_file(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
            print(contents)
    except FileNotFoundError:
        print('The file does not exist.')

print_file('cats.txt')
print()
print_file('dogs.txt')
