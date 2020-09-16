import json

# json_user.py and greet_user.py combined into one filename
# Commented out json_user.py code for convenience

"""
username = input('What is your name?\n')

filename = 'username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print('We\'ll remember you when you come back, ' + username + '.')
"""

filename = 'username.json'
with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back, " + username + "!")
