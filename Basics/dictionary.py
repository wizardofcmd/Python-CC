hisoka = {'first_name':'hisoka', 'last_name':'morrow', 'age':'unknown', 'city':'meteor city'}
for key in hisoka:
    print(hisoka[key])
print()

fav_numbers = {'sorin':10, 'gon':405, 'killua':99, 'hisoka':44, 'kurapika':404}
for key in fav_numbers:
    print(fav_numbers[key])
print()

glossary = {'loop':'iterate', 'variable':'stored data', 'boolean':'if something \
is true or false', 'tuple':'unchangeable piece of data'}
for key in glossary:
    print(key + ": " + glossary[key])
print()

rivers = {'nile':'egypt', 'amazon':'brazil', 'yangtze':'china'}
for key, value in rivers.items():
    print('The ' + key + ' runs through ' + value + '.')
print()
for key in rivers.keys():
    print(key)
print()
for value in rivers.values():
    print(value)
print()

favourite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
}

candidates = ['edward', 'jeremy', 'christi', 'kai', 'chrollo', 'jen']
for candidate in candidates:
    if candidate not in favourite_languages:
        print("You haven't taken our survey. Come and fill it out!")
    else:
        print("You have taken the survey already. Thank you.")
print()

# Storing dictionaries in a list.
chrollo = {'first_name':'chrollo', 'last_name':'lucilfer', 'age':'26', 'city':'meteor city'}
illumi = {'first_name':'illumi', 'last_name':'zoldyck', 'age':'24', 'city':'kukuroo mountain'}
people = [hisoka, chrollo, illumi]

for person in people:
    for field in person.values():
        print(field)
    print()

# Storing dictionaries in a dictionary
cities = {'london':{
        'country':'england',
        'population':'10,000,000',
        'fact':'home of chelsea fc'
        },

        'paris':{
        'country':'france',
        'population':'15,000,000',
        'fact':'has the eiffel tower'
        },

        'rome':{
        'country':'italy',
        'population':'20,000,000',
        'fact':'home of the colisseum'
        }
}

for city in cities:
    print('The city of ' + city + ':')
    print(cities[city])
