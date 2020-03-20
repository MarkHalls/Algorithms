#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    batches = None
    for key, value in recipe.items():
        # check that we have the ingredient
        if key in ingredients.keys():
            # update batch size based on smallest number of ingredients
            ing_batch = ingredients[key] // value
            if batches is None or ing_batch < batches:
                batches = ing_batch
        else:
            # if we don't have the ingredients we can't make the recipe
            batches = 0

    return batches


if __name__ == "__main__":
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {"milk": 100, "butter": 50, "flour": 5}
    ingredients = {"milk": 132, "butter": 48, "flour": 51}
    print(
        "{batches} batches can be made from the available ingredients: {ingredients}.".format(
            batches=recipe_batches(recipe, ingredients), ingredients=ingredients
        )
    )

