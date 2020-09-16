pizzas = ['Pepperoni', 'Mexican', 'Hawaii']
for pizza in pizzas:
    print('I like ' + pizza + ' pizza.')

print('\nI really love pizza!\n')

animals = ['Lion', 'Tiger', 'Panther']
for animal in animals:
    print('A ' + animal + ' would tear you apart easily.')

print("\nFor that reason, it's best to stay away.\n")

# 4-3 - 4-9, page 64
for value in range(1,21):
    print(value)
print()

'''
roundabout way of making a list of numbers oopsies.
million = []
for value in range(0, 1000001):
    million.append(value)
    print(million[value])
'''

million = [value for value in range (1,1000001)]
#for number in million:         Commented it out cause it would take too long to execute.
#    print(number)

print(min(million))
print(max(million))
print(sum(million))
print()

odd = [value for value in range(1,20,2)]
for number in odd:
    print(number)
print()

threes = [value for value in range(3,31,3)]
for three in threes:
    print(three)
print()

cubes = [value**2 for value in range(1,11)]
for number in cubes:
    print(number)
