"""
add the ability to keep track of the flesh color, rind color
and average weight
"""

DEFAULT_RIND_COLOR = 'white'
DEFAULT_AVG_WEIGHT = 0.5


# average weight of each melon is in pounds (lbs)
melons = {
    'Honeydew': {
        'price': 0.99,
        'seedless': True,
        'flesh color': DEFAULT_RIND_COLOR,
        'avg weight': DEFAULT_AVG_WEIGHT,
    },
    'Crenshaw': {
        'price': 2.00,
        'seedless': False,
        'flesh color': DEFAULT_RIND_COLOR,
        'avg weight': DEFAULT_AVG_WEIGHT,
    },
    'Crane': {
        'price': 2.50,
        'seedless': False,
        'flesh color': DEFAULT_RIND_COLOR,
        'avg weight': DEFAULT_AVG_WEIGHT,
    },
    'Casaba': {
        'price': 2.50,
        'seedless': False,
        'flesh color': DEFAULT_RIND_COLOR,
        'avg weight': DEFAULT_AVG_WEIGHT,
    },
    'Cantaloupe': {
        'price': 0.99,
        'seedless': False,
        'flesh color': DEFAULT_RIND_COLOR,
        'avg weight': DEFAULT_AVG_WEIGHT,
    },
}

def add_melon_property(new_property):
    """ add another property to each melon"""

    # Go through each melon
    for melon in melons:
        property_value = input(f'What is the value of {new_property} for {melon}? ')
        melons[melon][new_property] = property_value

        # Print the melon and new value to confirm
        print(f"{melon}'s {new_property} is set to {melons[melon][new_property]}.")




# melon_names = {
#     1: 'Honeydew',
#     2: 'Crenshaw',
#     3: 'Crane',
#     4: 'Casaba',
#     5: 'Cantaloupe',
# }

# melon_prices = {
#     1: 0.99,
#     2: 2.00,
#     3: 2.50,
#     4: 2.50,
#     5: 0.99,
# }

# melon_seedlessness = {
#     1: True,
#     2: False,
#     3: False,
#     4: False,
#     5: False,
# }
