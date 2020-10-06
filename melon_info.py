"""Print out all the melons in our inventory."""


from melons import melons_info


def print_melon(info_log):
    """Print each melon with corresponding attribute information."""
    for melon in info_log:
        print(f"{info_log[melon]}",
        f"price: {info_log[melon][price]}",
        f"seedless: {info_log[melon][seedless]}",
        f"flesh_color: {info_log[melon][flesh_color]}",
        f"weight: {info_log[melon][weight]}",
        f"rind_color: {info_log[melon][rind_color]}"
        )

print_melon(melons_info)