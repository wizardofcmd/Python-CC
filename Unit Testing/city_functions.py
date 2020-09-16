def format(city, country, population=''):
    """Generate a neatly formatted city and country"""
    if population:
        formatted = city + ', ' + country + ' - Population: ' + str(population)
    else:
        formatted = city + ', ' + country
    return formatted
