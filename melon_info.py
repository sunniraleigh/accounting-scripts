"""Print out all the melons in our inventory."""


from melons import melons_info


def print_melon(info_log):
    """Print each melon with corresponding attribute information."""
    for melon, attribute in info_log.items():
        print(f"{info_log[melon]}")

        for attribute, value in attribute.items():
            print(f"{attribute}: {value}")

print_melon(melons_info)