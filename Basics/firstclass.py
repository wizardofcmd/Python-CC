class Restaurant():
    """Class representing a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print('The name of the restaurant is ' + self.restaurant_name + '.')
        print('Cuisine: ' + self.cuisine_type + '.')

    def open_restaurant(self):
        print('\nThe restaurant is now open!')

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, number_served):
        if number_served > 0:
            self.number_served += number_served
        else:
            print("Can't serve minus people!")

restaurant = Restaurant('Luigis', 'Italian')
print(restaurant.restaurant_name + " " + restaurant.cuisine_type + \
" " + str(restaurant.number_served) + ".")
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.set_number_served(2)
print(str(restaurant.number_served))
restaurant.increment_number_served(4)
print(str(restaurant.number_served) + "\n")

class User():
    """Class representing a user profile with many attributes to describe them."""
    def __init__(self, first_name, last_name, age, height, eye_colour):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.eye_colour = eye_colour
        self.login_attempts = 0

    def describe_user(self):
        print(self.first_name + " " + self.last_name + " " + str(self.age) + " "\
        + self.height + " " + self.eye_colour + ".")
        # OR use __dict__, which prints the attributes and valuesof the class
        # in a dictionary format.
        print(self.__dict__)

    def greet_user(self):
        print('Hello ' + self.first_name + ', welcome.\n')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user = User('Kai', 'Havertz', 21, '189cm', 'Hazel')
user.describe_user()
user.greet_user()

print(user.login_attempts)
user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)
