class Restaurant():
    """Class representing a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('The name of the restaurant is ' + self.restaurant_name + '.')
        print('Cuisine: ' + self.cuisine_type + '.')

    def open_restaurant(self):
        print('\nThe restaurant is now open!')

restaurant = Restaurant('Luigis', 'Italian')
print(restaurant.restaurant_name + " " + restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
