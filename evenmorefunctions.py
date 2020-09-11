def sandwich_maker(*toppings):
    print('You ordered a sandwich with:')
    for topping in toppings:
        print('- ' + topping)
    print()
sandwich_maker('cheese', 'tomato', 'lettuce', 'bacon')
sandwich_maker('egg', 'mayo')

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('sorin', 'morrow',
                            location = 'london',
                            field = 'computer science',
                            favourite_anime = 'code geass')
print(user_profile)
print()

def make_car(brand, model, **car_info):
    car = {}
    car['brand'] = brand
    car['model'] = model
    for key, value in car_info.items():
        car[key] = value
    return car

user_car = make_car('audi', 'r8', engine = 'v12', seats = '5', seatbelts = True)
print(user_car)
print()
