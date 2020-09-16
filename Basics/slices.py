foods = ['pizza', 'ice cream', 'burger', 'chips', 'ch*cken wings']
print('The first three items in the list are:')
print(foods[0:3])

print('\nThe middle three items in the list are:')
print(foods[1:4])

print('\nThe last three items in the list are:')
print(foods[-3:]) # or you can use print(foods[3:5])

food_copy = foods[:]
foods.append('tacos')
food_copy.append('burrito')

print('\nMy favourite foods are:')
print(foods)

print('\Your favourite foods are:')
print(food_copy)

print()
for food in foods:
    print(food)

print()
for food in food_copy:
    print(food)
