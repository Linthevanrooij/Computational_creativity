import random
import json

# Load ingredient data from the JSON file
with open('ingredients.json', 'r') as f:
    ingredients_data = json.load(f)
extra_filling_ingredients_cooked = ingredients_data['extra_filling_ingredients_cooked']
extra_filling_ingredients_uncooked = ingredients_data['extra_filling_ingredients_uncooked']
main_filling_ingredients = ingredients_data['main_filling_ingredients']
dough_ingredients_cooked = ingredients_data['dough_ingredients_cooked']
dough_ingredients_uncooked = ingredients_data['dough_ingredients_uncooked']
flour_ingredients = ingredients_data['flour_ingredients']
optional_ingredients = ingredients_data['optional_ingredients']

# Randomly choose ingredients
extra_filling_ingredient_cooked = random.choice(extra_filling_ingredients_cooked)
extra_filling_ingredient_uncooked = random.choice(extra_filling_ingredients_uncooked)
main_filling_ingredient = random.choice(main_filling_ingredients)
dough_ingredient_cooked = random.choice(dough_ingredients_cooked)
dough_ingredient_uncooked = random.choice(dough_ingredients_uncooked)
flour_ingredient = random.choice(flour_ingredients)
optional_ingredient = random.choice(optional_ingredients)

# Randomly select either cooked or uncooked filling ingredient
if random.choice([True, False]):
    filling_step = f"1. Cook the {extra_filling_ingredient_cooked} and blend or mash into a puree."
    chosen_filling_ingredient = extra_filling_ingredient_cooked
else:
    filling_step = f"1. Blend or mash the {extra_filling_ingredient_uncooked} into a puree."
    chosen_filling_ingredient = extra_filling_ingredient_uncooked

# Randomly select either cooked or uncooked dough ingredient
if random.choice([True, False]):
    dough_step = f"4. Cook the {dough_ingredient_cooked} and blend or mash it into a puree."
    chosen_dough_ingredient = dough_ingredient_cooked
else:
    dough_step = f"4. Blend or mash the {dough_ingredient_uncooked} into a puree."
    chosen_dough_ingredient = dough_ingredient_uncooked

# Randomly select final instructions
final_step = random.choice([
    "13. Dust the finished mochi with more corn starch.",
    "13. Cover the finished mochi with melted chocolate and put it in the fridge to harden."
])

# Ingredient list template
ingredient_list = f"""
Ingredients:
- {chosen_filling_ingredient}
- {main_filling_ingredient}
- {chosen_dough_ingredient}
- {flour_ingredient}
- {optional_ingredient}
"""

# Recipe template
recipe_template = f"""
{ingredient_list}

Prepare the mochi filling:

{filling_step}
2. In a small bowl, mix the {chosen_filling_ingredient} with {main_filling_ingredient}.
3. Portion out (8?) scoops of filling, by using a tablespoon or a cookie scoop, and set aside.

Prepare the mochi dough:

{dough_step}
5. In a microwave-safe bowl, mix the {chosen_dough_ingredient} puree with {flour_ingredient} and {optional_ingredient}.
6. Microwave the combined dough in the microwave for 90 to 120 seconds.
7. Use a solid metal spoon to stir the mochi mixture so that the cooked and uncooked parts are evenly mixed.
8. Microwave the mochi dough mixture again, this time for 1 minute. You'll know when it is ready when the dough is slightly translucent and glossy.

Making the mochi:

9. Drop the hot mochi dough onto a surface floured with corn starch.
10. Use a rolling pin or your hands to flatten it into a sheet.
11. Cut the mochi dough into (8?) pieces using a dough cutter or scissors.
12. Place a scoop of prepared filling on the dough and wrap the mochi dough around the filling.
{final_step}
14. Enjoy!
"""

# Print the generated recipe
print(recipe_template)
