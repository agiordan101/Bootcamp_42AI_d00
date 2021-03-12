cookbook = {
    "sandwich": {
                    "list": ("ham", "bread", "cheese", "tomatoes"),
                    "meal": "lunch",
                    "prep_time": 10
                },
    "cake": {
                "list": ("flour", "suger", "eggs"),
                "meal": "dessert",
                "prep_time": 60
            },
    "salad": {
                "list": ("avocado", "arugula", "tomatoes", "spinach"),
                "meal": "lunch",
                "prep_time": 15
             }
}


def add_recipe(name, ingredients, meal, prep_time):
    cookbook[name] = {
                        "list": ingredients,
                        "meal": meal,
                        "prep_time": prep_time
                     }
    print("A new recipe has been created.")
    print_recipe(name)


def delete_recipe(name):
    del cookbook[name]
    print("Recipe {} has been deleted".format(name))


def print_recipe(name):
    print("Recipe for {}:".format(name))
    print("Ingredients list: {}.".format(cookbook.get(name).get("list")))
    print("To be eaten for {}.".format(cookbook.get(name).get("meal")))
    print("Takes {} minutes of cooking.\
    ".format(cookbook.get(name).get("prep_time")))


def print_all_recipe():
    for cle in cookbook.keys():
        print_recipe(cle)
        print()


exitLoop = False
while exitLoop is False:
    print()
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")
    answer = input("> ")
    print()

    if str.isnumeric(answer) is False or int(answer) < 0 or int(answer) > 5:
        print("Please enter a number between 1 and 5.")
        exitLoop = True
    elif int(answer) == 4:
        print_all_recipe()
    elif int(answer) == 5:
        exitLoop = True
    else:
        recipe = input("Please enter the recipe's name: ")
        if int(answer) != 1 and (recipe in cookbook) is False:
            print("Please enter an existing recipe.")
            exitLoop = True
        elif int(answer) == 1:
            ingredients = []
            while len(ingredients) == 0 or ingredients[-1] != "exit":
                ingredients.append(input("Add a new ingredient ?\
 (Enter exit to stop): "))
            del ingredients[-1]
            meal = input("It's a meal for: ")
            prep_time = input("Its preparation times is: ")
            add_recipe(recipe, ingredients, meal, prep_time)
        elif int(answer) == 2:
            delete_recipe(recipe)
        elif int(answer) == 3:
            print_recipe(recipe)
print("Cookbook closed.")
