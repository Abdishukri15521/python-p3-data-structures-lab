
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
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    matching_foods = [food for food in spicy_foods if food["cuisine"] == cuisine]
    return matching_foods[0] if matching_foods else None

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

def get_average_heat_level(spicy_foods):
    heat_levels = [food["heat_level"] for food in spicy_foods]
    return sum(heat_levels) / len(heat_levels) if heat_levels else 0

def create_spicy_food(spicy_foods, spicy_food):
    return spicy_foods + [spicy_food]

class TestDataStructures:
    SPICY_FOODS = spicy_foods

class TestGetNames:
    def test_get_names(self):
        assert get_names(TestDataStructures.SPICY_FOODS) == ['Green Curry', 'Buffalo Wings', 'Mapo Tofu']

class TestGetSpiciestFoods:
    def test_get_spiciest_foods(self):
        assert get_spiciest_foods(TestDataStructures.SPICY_FOODS) == [{'name': 'Green Curry', 'cuisine': 'Thai', 'heat_level': 9}, {'name': 'Mapo Tofu', 'cuisine': 'Sichuan', 'heat_level': 6}]

class TestPrintSpicyFoods:
    def test_print_spicy_foods(self):
        captured_out = io.StringIO()
        sys.stdout = captured_out
        print_spicy_foods(TestDataStructures.SPICY_FOODS)
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Green Curry (Thai) | Heat Level: 🌶🌶🌶🌶🌶🌶🌶🌶🌶\nBuffalo Wings (American) | Heat Level: 🌶🌶🌶\nMapo Tofu (Sichuan) | Heat Level: 🌶🌶🌶🌶🌶🌶\n"

class TestGetSpicyFoodByCuisine:
    def test_get_spicy_food_by_cuisine(self):
        assert get_spicy_food_by_cuisine(TestDataStructures.SPICY_FOODS, "American") == {'name': 'Buffalo Wings', 'cuisine': 'American', 'heat_level': 3}

class TestPrintSpiciestFoods:
    def test_print_spiciest_foods(self):
        captured_out = io.StringIO()
        sys.stdout = captured_out
        print_spiciest_foods(TestDataStructures.SPICY_FOODS)
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Green Curry (Thai) | Heat Level: 🌶🌶🌶🌶🌶🌶🌶🌶🌶\nMapo Tofu (Sichuan) | Heat Level: 🌶🌶🌶🌶🌶🌶\n"

class TestGetAverageHeatLevel:
    def test_get_average_heat_level(self):
        assert get_average_heat_level(TestDataStructures.SPICY_FOODS) == 6

class TestCreateSpicyFood:
    def test_create_spicy_food(self):
        new_spicy_foods = create_spicy_food(
            TestDataStructures.SPICY_FOODS,
            {
                'name': 'Griot',
                'cuisine': 'Haitian',
                'heat_level': 10,
            }
        )
        assert new_spicy_foods == [{'name': 'Green Curry', 'cuisine': 'Thai', 'heat_level': 9}, {'name': 'Buffalo Wings', 'cuisine': 'American', 'heat_level': 3}, {'name': 'Mapo Tofu', 'cuisine': 'Sichuan', 'heat_level': 6}, {'name': 'Griot', 'cuisine': 'Haitian', 'heat_level': 10}]
