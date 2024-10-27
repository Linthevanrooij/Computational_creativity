# Logbook of Computational Creativity Bitwise Bakeoff

## Initial Idea 
_16.10.2024_

Our initial idea for the Bitwise Bakeoff was to create a mochi recipe generator. Mochi is a traditional Japanese food made from glutinous rice, known as mochigome in Japanese. This soft, chewy dough forms a rice cake that can be wrapped around various fillings. There are many variations of mochi, as it can be filled with ingredients like red bean paste or ice cream. Mochi flavours can be both sweet and savoury. Because of this flavour variety, we thought mochi would be the perfect food as an inspiring set for a recipe generator.

We plan to use [this](https://allpurposeveggies.com/12967/12-mochi-flavors-easy-recipes-for-mochi-ice-cream-and-more/) and [this website](https://thericechick.com/mochi-recipes/) for our initial set of inspiring recipes. 

Additionally, to generate unique and unusual mochi flavours, we planned to create our own list of ingredients to combine with mochi. To calculate the fitness of each ingredient, from both the external recipe sources and our own list, we used the ratings (1 to 5 stars) from the existing recipes. For each ingredient found in a recipe, we assigned it the recipe’s rating. If an ingredient appeared multiple times among all recipes, we will use the average rating. For ingredients from our own list, we rated them ourselves and calculated the average score based on our ratings.

Since mochi is originally from Japan, for the presentation of our recipes we liked to maintain the Japanese style. Therefore, we planned to use a [text generator](https://lingojam.com/JapaneseText) that creates text from Japanese symbols, like 爪ㄖ匚卄丨, and used this font for the titles of the recipes. Another idea is to present the recipes in a kawaii style. Kawaii is a part of Japanese culture that emphasizes cuteness. We can achieve this by creating AI-generated images of cartoonish cute mochi designs that match the ingredients in the recipe and using soft pastel colours associated with a kawaii drawing style for the cookbook. We wanted to create a tiny pocket cookbook as that would make it instantly cute and it would fit well within our Japanese mochi theme. Moreover, we wanted to use generative AI to create fitting titles for the mochi recipes. We hand-designed the cookbook and used placeholders for the ingredients, instructions and images of the generated recipe.
We aim at increasing the perceived value of the recipes by staying within this Japanese-themed presentation for the Mochi cookbook.

https://www.canva.com/design/DAGUYibnRzg/cqlxfxbQ7bQ5u21EhB991g/edit?utm_content=DAGUYibnRzg&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton


### Updates on idea/new goals
_23.10.2024_

At some point we realised that by adding our list of random ingredients, we would essentially be creating monsterous mochi. This sounded quite nice to us and resulted in the renaming of our project from "Cookie monsters" to "Mochi Monsters". Thus, the title of our cookbook will be Mochi Monsters.

## Inspiring set & creation of knowledge base
_16.10.2024_
We gathered recipes for our inspiring set using two different websites with both around 20 different mochi recipes as our inspiring set. We webscraped the recipes and created our own database with it.
We decided that besides existing recipes, we wanted to add some loose ingredients and named this our "weird ingredient list", as we were interested in adding ingredients that you would normally not associate with mochi. For this list, each of us added some unexpected ingredients and rated them on a 1 to 5 scale for the fitness function. Some of the recipes from the two websites we used in our inspiring set also did not have a rating, therefore, we gave them our own rating as well. 

_21.10.2024_
Additionally, due to allergies, we created a class of ingredients that contains nuts, peanuts, and gluten. To normalise every recipe we standardised every recipe to a serving of 10 mochis and converted every unit to grams.

## Implementation recipe generator
_21.10.2024_


_Whichever way you go with the implementation, think about the stopping criteria for your genetic algorithm and what you want your system to output at the end of a run, e.g., should your system run for a fixed number of generations and return the best recipe found so far, or should its run be controlled interactively by a user._

### The fitness criteria
_16.10.2024_

At first, we wanted to use "rating" as our evaluative criterium. We wrote a fitness function where only the best rated ingredients would fit in the recipe. The best recipe rating would have the highest average rating.

_21.10.2024_

We noticed that by using only the rating, that it ended up generating recipes that used only ingredients with a rating of 5. This meant that most ingredients were automatically excluded, and thus also the possibility of a "surprising" recipe. For that reasing we decided to add a random evaluative criterium (such as "length of ingredient list" in the simple PIERRE example). We settled on using the amount of consonants in an ingredient. We gave weights to each criteria, with rating a weiht of 0,1 and consonants a weight of 0,9.
Moreover, the fitness function excludes ingredients containing gluten or nuts by ascribing them with a value of 0.

_23.10.2024_

After giving the fitness function some thought, we figured that ingredients with long names would automatically be chosen over ingredients with short names. We decided to calculate the average number of consonants in a recipe. Furthermore, what is important to make mochi, is that it contains (one) flour. That is why we incorporated this into the fitness function, where fitness is set to 0 if the recipe contains no flour or more than one flour. Since we are making mochi balls that do not need to be baked, we also set the fitness to 0 when eggs and baking powder were included in the recipe. Finally, the fitness is set to zero when allergens are included. This led to the following fitness function:
- The number of consonants with a weight of 0,9.
- The rating of the recipe with a weight of 0.1.
- The presence of 1 flour (binary),
- The presence of eggs or baking powder (binary).
- The presence of ingredients that are categorised as allergens (|binary).

```r['fitness'] = (rating*0.9 + cons*0.1) * flour_presence * forbid```

All binary factors were combined as "forbidden" factors in our fitness function.

_26.10.2024_

We found out that basing the fitness of the average amount of consonants did not give very inspiring recipes: it still used the ingredient with the longest name.
Also, it produced recipes with only that ingredient, as adding others would bring the average amount of consonants down. We added to our fitness function that any difference in a length of 7 ingredients would result in a penalty, lowering the fitness, just to see if it would make a difference. The recipes that came out were better already. However, the consonant criterium limited our ingredients to a small sample, so we removed the consonant criterium from our fitness function.

Moreover, after going through many recipes, we learned that the base ingredient of a mochi is not only flour, but flour in combination with either a liquid or a puree in combination with a liquid. Also, that butter is not used in the dough, only possibly in the filling. 

We realised that 7 is maybe a bit of a random number, so we argued that it is nice to make it a range. The minimum amount of ingredients necessary to make mochi is 3 (a flour, a liquid, and a filling). This little ingredients would not spark exciting recipes. We thus chose to set the minimum of ingredients to 5, since we are building a creative system. With too many ingredients, the individual ingredients might lose their flavour. Thus, we settled on a maximum of 8 ingredients. We chose a range of 4 to 8 ingredients. With a length smaller than 3 ingredients, it would not be a mochi, and therefore it would be excluded, and above 8 we included a penalty. 

Therefore, we made some adjustments to our fitness function:
- The rating of the recipe
- The presence of 1 flour (binary),
- The presence of eggs or baking powder (binary).
- The presence of ingredients that are categorised as allergens (|binary).
- The presence of max 1 butter
- The presence of min 1 liquid OR puree, with a min of 1 and a max of 2 liquids.

```r['fitness'] = max(0, scaled_rating - length_penalty - ingredient_constraint)*forbid*dough_presence```

### Mutations
_16.10.2024_

As possible mutations we used addition, substitution and deletion of ingredients.

### Normalisation
_25.10.2024_

We had not thought of how we wanted to normalise our recipes. The only possible solution was to try out some existing mochi and base our answer on that. As a result, we decided that we wanted each of our mochi to weigh around 50 grams (as our try-out mochi weighed 35 grams and were a bit scanty to our taste). As we generate recipes for 10 servings we decided that we would normalise it to 500 grams of total ingredient weight.

## Limitations
Some recipes from the inspiring set did not have a rating. We solved this by adding our own rating, based on our own liking of the ingredients. We then took the average of our ratings for the recipes. 
Another problem with the recipes from the inspring set was the ingredients were measured in different units (e.g., cups, ounces, and grams). To achieve a recipe that takes into account a correct ratio of the ingredients, we converted all the units to grams and ml by using the library Sugarcube. This library already contained the density of the products water, sugar, flour, butter, and salt, therefore these ingredients were automatically converted. For the density of other ingredients, we categorised them in classes, such as liquid for milks and sauces, and gave them a general density based on information online. After catergorising all the ingredients, we added their densities to the library, whereafter the units were converted.
On top of that, there were some measuring units that were difficult to convert or normalise, such as "a pinch" or "a whole/large (egg)". Moreover, sometimes an ingredient was a flour "to dust the surface". We chose to exclude those ingredients.


## Reflection on the question of how to evaluate the creativity of your system 

For the evaluation of our recipe generator we are thinking of doing the Lovelace 2.0 test, where an artifical system is evaluated by a set of constraints.



