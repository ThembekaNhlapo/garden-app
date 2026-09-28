# Hardcoded values for the season and plant type
season = input("Enter the season (summer/winter): ")
plant_type = input("Enter the plant type (flower/vegetable): ")

def get_season_advice(season):
    """Return gardening advice based on the season."""
    if season == "summer":
        return "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        return "Protect your plants from frost with covers.\n"
    else:
        return "No advice for this season.\n"


def get_plant_advice(plant_type):
    """Return gardening advice based on the plant type."""
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    else:
        return "No advice for this type of plant."


# Generate the full advice message
advice = get_season_advice(season) + get_plant_advice(plant_type)

# Print the generated advice
print(advice)

# TODO: Examples of possible features to add:
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.