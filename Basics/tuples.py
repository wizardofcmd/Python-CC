buffet = ('curry', 'chicken balls', 'kung pao', 'orange chicken', 'sweet chilli')
for food in buffet:
    print(food)
print()

# Will not work because tuples are immutable
# buffet[0] = 'pizza'

# Redifining a whole tuple is allowed though
buffet = ('egg fried rice', 'chicken balls', 'kung pao', 'orange chicken', 'sweet chilli')
for food in buffet:
    print(food)
