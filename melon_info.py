"""Print out all the melons in our inventory."""


from melons import melons


def print_melon():
    """Print each melon with corresponding attribute information."""

    # Go through the melons dictionary
    for melon, details in melons.items():

        # Print uppercase melon name
        print(melon.upper())

        for detail, value in details.items():
            print(f"    {detail}: {value}")

        # Divider between melons
        print('=============================')


print_melon()





#     have_or_have_not = 'have'
#     if seedless:
#         have_or_have_not = 'do not have'

#     print(f'{name}s {have_or_have_not} seeds and are ${price:.2f}')


# for i in melon_names:
#     print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])
