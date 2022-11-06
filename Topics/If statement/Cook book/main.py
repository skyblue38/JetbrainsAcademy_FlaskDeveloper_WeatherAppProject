pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"

recipes = [pasta, apple_pie, ratatouille, chocolate_cake, omelette]
recipe_name = ["pasta", "apple pie", "ratatouille", "chocolate cake", "omelette"]
ingredient = input()
rn = 0
for r in recipes:
    if ingredient in r:
        print("{} time!".format(recipe_name[rn]))
    rn += 1
