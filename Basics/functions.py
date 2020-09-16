def display_message():
    print("I am learning about functions in this chapter.")
display_message()

def favourite_book(title):
    print(title + " is my favourite book.")
favourite_book('Aeneid')
print()

def make_shirt(shirt_size, shirt_msg):
    print('The shirt size is ' + shirt_size + ' and the message printed on is ' + '\'' + shirt_msg + '\'' + '.')
make_shirt('Medium', 'Havertz is the GOAT')
make_shirt(shirt_size = 'Large', shirt_msg = 'Werner awaits greatness')
print()

def city_country(city, country):
    message = city + ', ' + country
    return message
print('Enter \'quit\' at either input to exit.')

while True:
    user_country = input("Enter a country. ")
    if user_country.lower() == 'quit':
        break
    user_city = input("Enter a city in said country. ")
    if user_city.lower() == 'quit':
        break
    full_answer = city_country(user_city, user_country)
    print(full_answer)
print()

album_dict = {}
album_list = []
def make_album(album_title, artist, tracks=''):
    album_dict = {'album_title':album_title, 'artist':artist}
    # OR album_dict['album_title'] = album_title
    # OR album_dict['artist'] = artist
    if tracks:
        album_dict['tracks'] = int(tracks)
    return album_dict

print('Enter \'quit\' at either input to exit.')
while True:
    user_title = input('Enter an album title. ')
    if user_title.lower() == 'quit':
        break
    user_artist = input('Enter an artist name. ')
    if user_artist.lower() == 'quit':
        break
    user_tracks = input('Enter the amount of tracks if you wish. ')
    if user_tracks.lower() == 'quit':
        break
    album = make_album(user_title, user_artist, user_tracks)
    album_list.append(album)
    repeat = input("Do you want to add another album? Type yes or no. ")
    if repeat.lower() == 'no':
        break
    print()
print(album_list)
