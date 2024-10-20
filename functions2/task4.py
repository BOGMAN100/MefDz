
in_stock = {}

def order(*preferences):
    # Рецепты напитков
    recipes = {
        "Эспрессо": {"coffee": 1, "milk": 0, "cream": 0},
        "Капучино": {"coffee": 1, "milk": 3, "cream": 0},
        "Макиато": {"coffee": 2, "milk": 1, "cream": 0},
        "Кофе по-венски": {"coffee": 1, "milk": 0, "cream": 2},
        "Латте Макиато": {"coffee": 1, "milk": 2, "cream": 1},
        "Кон Панна": {"coffee": 1, "milk": 0, "cream": 1}
    }

    for preference in preferences:
        
        if preference in recipes:
            
            required = recipes[preference]
            
            if (in_stock["coffee"] >= required["coffee"] and
                in_stock["milk"] >= required["milk"] and
                in_stock["cream"] >= required["cream"]):
                
                in_stock["coffee"] -= required["coffee"]
                in_stock["milk"] -= required["milk"]
                in_stock["cream"] -= required["cream"]
                return preference

    return "К сожалению, не можем предложить Вам напиток"


in_stock = {"coffee": 1, "milk": 2, "cream": 3}
print(order("Эспрессо", "Капучино", "Макиато", "Кофе по-венски", "Латте Макиато", "Кон Панна"))
print(order("Эспрессо", "Капучино", "Макиато", "Кофе по-венски", "Латте Макиато", "Кон Панна"))

in_stock = {"coffee": 4, "milk": 4, "cream": 0}
print(order("Капучино", "Макиато", "Эспрессо"))
print(order("Капучино", "Макиато", "Эспрессо"))
print(order("Капучино", "Макиато", "Эспрессо"))