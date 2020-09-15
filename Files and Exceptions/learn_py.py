filename = 'learning_python.txt'
with open(filename) as file_object:
    contents = file_object.read()
    print(contents + "\n")

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
    print()

with open(filename) as file_object:
    lines = file_object.readlines()

    for line in lines:
        print(line.rstrip())
    print()

with open(filename) as file_object:
    lines = file_object.readlines()
    for line in lines:
        line = line.replace('Python', 'C')
        print(line.rstrip())
