#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  min = float("inf")
  if recipe.keys() == ingredients.keys():
    for item in recipe.keys():
      if min > ingredients[item] // recipe[item]:
        min = ingredients[item] // recipe[item]

  if min == float("inf"):
    min = 0
  return min  


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))