# List of ingredients that need to be cooked or mashed ??????????
cooking_ingredients = ['potato', 'broccoli', 'eggplant']
mashing_ingredients = ['mango', 'banana', 'lychee', 'strawberry']

# Example generated ingredient list
generated_ingredients = ['honey', 'banana', 'glutinous rice flour', 'sugar', 'eggplant']

# Classify ingredients
def classify_ingredients(ingredients):
    flour_ingredient = None
    non_flour_ingredients = []

    # Find ingredients that contain "flour"
    for ingredient in ingredients:
        if "flour" in ingredient.lower():
            flour_ingredient = ingredient
        else:
            non_flour_ingredients.append(ingredient)

    # Check if ingredients list contains flour
    if not flour_ingredient:
        raise ValueError("No flour ingredient found in the generated ingredients list!")

    # Classifiy other ingredients as ingredient1 to ingredient4
    ingredient1, ingredient2, ingredient3, ingredient4 = non_flour_ingredients
    
    
    return flour_ingredient, ingredient1, ingredient2, ingredient3, ingredient4

flour_ingredient, ingredient1, ingredient2, ingredient3, ingredient4 = classify_ingredients(generated_ingredients)

# Check if ingredient1 to 4 are cooking or mashing ingredients
def preparation_step(ingredient, cooking_list, mashing_list):
    if ingredient in cooking_list:
        return f"Cook the {ingredient} and blend or mash into a puree."
    elif ingredient in mashing_list:
        return f"Blend or mash the {ingredient} into a puree."
    else:
        return ""  # No extra step when ingredient does not need to be cooked or mashed

# Check if preparation step needs to be added
step1 = preparation_step(ingredient1, cooking_ingredients, mashing_ingredients)
step2 = preparation_step(ingredient2, cooking_ingredients, mashing_ingredients)
step3 = preparation_step(ingredient3, cooking_ingredients, mashing_ingredients)
step4 = preparation_step(ingredient4, cooking_ingredients, mashing_ingredients)

# Recept template
recipe_template = """
Prepare the mochi filling:

{step1}
{step2}
In a small bowl, mix the {ingredient1} with the {ingredient2}.
Portion out 8 scoops of filling, using a tablespoon or a cookie scoop, and set aside.

Prepare the mochi dough:

{step3}
{step4}
In a microwave-safe bowl, mix the {ingredient3} with the {ingredient4} and {flour_ingredient}.
Microwave the combined dough for 90 to 120 seconds.
Stir the mochi mixture so the cooked and uncooked parts are evenly mixed.
Microwave again for 1 minute until the dough is slightly translucent and glossy.

Making the mochi:

Drop the hot mochi dough onto a surface floured with corn starch.
Use a rolling pin or your hands to flatten it into a sheet.
Cut the dough into 8 pieces using a dough cutter or scissors.
Place a scoop of prepared filling on each piece and wrap the mochi dough around the filling.
Enjoy!
"""

# Fill in template
recipe_filled = recipe_template.format(
    step1=step1,
    step2=step2,
    step3=step3,
    step4=step4,
    ingredient1=ingredient1,
    ingredient2=ingredient2,
    ingredient3=ingredient3,
    ingredient4=ingredient4,
    flour_ingredient=flour_ingredient
)

# Print generated recipe
print(recipe_filled)
