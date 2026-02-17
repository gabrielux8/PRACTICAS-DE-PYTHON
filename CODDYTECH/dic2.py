recipe_book = {
    "Pancakes": ["flour", "milk", "eggs", "sugar"], 
    "Salad": ["lettuce", "tomato", "cucumber", "olive oil"]
}

print(recipe_book["Pancakes"])
recipe_book["Smoothie"] = ["banana", "milk", "honey"]
cadena = recipe_book["Smoothie"]
cadena.append("blueberries")
print(recipe_book)