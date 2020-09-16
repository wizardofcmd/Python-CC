magicians = ['Houdini', 'Dynamo', 'Hisoka']
magicians_copy = magicians[:]

def show_magicians(magicians):
    for magician in magicians:
        print(magician)
    print()

def make_great(magicians):
    for magician in magicians:
        current_magician = magicians.pop(-len(magicians))
        current_magician = 'Great ' + current_magician
        magicians.append(current_magician)
    print()

make_great(magicians_copy)
show_magicians(magicians)
show_magicians(magicians_copy)
