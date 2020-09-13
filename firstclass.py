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

class User():
    """Class representing a user profile with many attributes to describe them."""
    def __init__(self, first_name, last_name, age, height, eye_colour):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.eye_colour = eye_colour

    def describe_user(self):
        print(self.first_name + " " + self.last_name + " " + str(self.age) + " "\
        + self.height + " " + self.eye_colour + ".")
        # OR use __dict__, which prints the attributes and valuesof the class
        # in a dictionary format.
        print(self.__dict__)

    def greet_user(self):
        print('Hello ' + self.first_name + ', welcome.')

user = User('Kai', 'Havertz', 21, '189cm', 'Hazel')
user.describe_user()
user.greet_user()
