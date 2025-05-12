spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [spicy_food["name"] for spicy_food in spicy_foods]
    return names

def get_spiciest_foods(spicy_foods):
    return [spicy_food for spicy_food in spicy_foods if spicy_food["heat_level"] > 5]
    pass

def print_spicy_foods(spicy_foods):
    for spicy_food in spicy_foods:
        heat = "🌶" * spicy_food["heat_level"]
        print(f"{spicy_food['name']} ({spicy_food['cuisine']}) | Heat Level: {heat}")
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for spicy_food in spicy_foods:
        if spicy_food["cuisine"] == cuisine:
            return spicy_food
    return None
    pass

def print_spiciest_foods(spicy_foods):
    for spicy_food in spicy_foods:
        if spicy_food["heat_level"] > 5:
            heat = "🌶" * spicy_food["heat_level"]
            print(f"{spicy_food['name']} ({spicy_food['cuisine']}) | Heat Level: {heat}")
    pass

def get_average_heat_level(spicy_foods):
    total_heat = sum(spicy_food["heat_level"] for spicy_food in spicy_foods)
    average_heat = total_heat / len(spicy_foods)
    return average_heat
    pass

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    pass
