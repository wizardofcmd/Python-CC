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
        print(self.first_name + " " + self.last_name + " " + str(self.age) + " "
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

class IceCreamStand(Restaurant):
    """Subclass of restaurant, representing an ice cream stand"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes of the parent class.
        Then initialize attributes specific to the child class.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry', 'coconut']

    def display_flavors(self):
        for flavor in self.flavors:
            print(flavor)
        print()

class Admin(User):
    def __init__(self, first_name, last_name, age, height, eye_colour):
        super().__init__(first_name, last_name, age, height, eye_colour)
        self.privileges = Privilege()

class Privilege():
    def __init__(self):
        self.privileges = ['can add post',
        'can delete post',
        'can ban user',
        'can create user']

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)
        print()
"""
icecream = IceCreamStand('Peach', 'Ice Cream')
icecream.display_flavors()

admin = Admin('Kai', 'Havertz', 21, '189cm', 'Hazel')
admin.privileges.show_privileges()
"""
