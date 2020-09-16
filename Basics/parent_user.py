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
