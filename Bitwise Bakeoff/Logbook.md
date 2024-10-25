# Log file of Computational Creativity Bitwise Bakeoff

## Initial Idea  
Our initial idea for the Bitwise Bakeoff is to create a mochi recipe generator. Mochi is a traditional Japanese food made from glutinous rice, known as mochigome in Japanese. This soft, chewy dough forms a rice cake that can be wrapped around various fillings. There are many variations of mochi, as it can be filled with ingredients like red bean paste or ice cream. Mochi flavours can be both sweet and savoury. Because of this flavour variety, we thought mochi would be the perfect food as a inspiring set for a recipe generator.

We plan to use [this](https://allpurposeveggies.com/12967/12-mochi-flavors-easy-recipes-for-mochi-ice-cream-and-more/) and [this website](https://thericechick.com/mochi-recipes/) for our initial set of inspiring recipes:


Additionally, to generate unique and unusual mochi flavours, we plan to create our own list of inspiring ingredients to combine with mochi. To calculate the fitness of each ingredient, from both the external recipe sources and our own list, we will use the ratings (1 to 5 stars) from the existing recipes. For each ingredient found in a recipe, we will assign it the recipe’s rating. If an ingredient appears multiple times, we will use the average rating. For ingredients from our own list, we will rate them ourselves and calculate the average score based on the three of us.

For the presentation of our recipes, we like to maintain the Japanese style. Therefore, we plan to use a [text generator](https://lingojam.com/JapaneseText) that creates Japanese-like symbols from standard text, like 爪ㄖ匚卄丨, and use this for the instructions and ingredient list of the recipe. Another idea is to present the recipes in a kawaii style. Kawaii is a part of Japanese culture that emphasizes cuteness. We can achieve this by creating AI-generated images of cute mochi designs that match the ingredients in the recipe.

## Updates on idea/new goals
23/10/2024
The title of our 'cookbook' will be Mochi Monsters. This refers to the term 'Cookie Monster', only replacing Mochi with Cookie. Besides, it will also match the images of the mochi's in the recipes, because we are planning to make 'kawaii' mochis, which will have faces, so it will be cute mochi monsters.

For the evaluation of our recipe generator we are thinking of doing the Lovelace 2.0 test, where an artifical system is evaluated by a set of constraints. 


The following constraints will be used to evaluate our mochi generator:





## Step-by-step account on how to tackled tasks (inspiring set, implement recipe generator, presentation) + reflection on development

### Inspiring set: 
We used two different websites with both around 20 different mochi recipes as our inspiring set. To generate new recipes with weird, unexpected ingredients, we make our own weird ingredient list. For this list, each of us added some crazy ingredients that we would like to combine with mochi and rated them on a 1 to 5 scale for the fitness function. Some of the recipes from the two websites we used in our inspiring set also did not have a rating, therefore, we gave them our own rating as well. Additionally, due to allergies, we created a class of ingredients that contain nuts, peanuts, and gluten. To normalise every recipe we standardised every recipe to a serving of 10 mochis and converted every unit to grams.



### Implementation recipe generator
blabla

### The fitness criteria
To evaluate the recipes, we created a fitness function based on:
- The number of consonants with a weight of 0,9.
- The rating of the recipe with a weight of 0.1.
- The presence of flour, eggs, baking powder (binary).
- The presence of ingredients that are categorised as allergens (|binary).

The main criteria to generate new recipes are the number of consonants and rating. To calculate the number of consonants, we calculated the average number of consonants. (sum of all consonants / n ingredients). To calculate the rating of the recipe we calculated the average rating of all ingredients (sum of ratings / n ingredients). These do not take into account the ingredients containing nuts, peanuts, and gluten.

Furthermore, what is important to make mochi, is that it contains (one) flour. That’s why we incorporated this into the fitness function, where fitness is set to zero if the recipe contains no flour or more than one flour. Since we are making mochis balls that do not need to be baked, we also set the fitness to zero when eggs and baking powder are included in the recipe. Finally, the fitness is set to zero when allergens are included.

### Mutations
Additions, substitution, deletion, 

Normalisation: we decided that we wanted each of our mochi to weigh around 50 grams (as our try-out mochi weighed 35 grams and was a bit scanty to our taste). As we create recipes for 10 servings we decided that we would normalise the generated recipes by normalising it to 500 grams of total ingredient weight.

### Limitations that we encountered
During the implementation of the fitness function, were not sure if using simply the rating would result in new recipes, since an evolution algorithm would then just give recipes with the highest rated ingredients, and the non-rated and lower rated ingredients would not stand a chance. Therefore, we started looking into other fitness criteria. We thought about the ingredient being vegan/vegetarian/gluten-free or cooking time. We argued that we needed to find a criterium that has nothing to do with the quality of the ingredient itself (such as length of ingredients in the example code). But since a rating of a recipe (and thus an ingredient) does possibly say something about the goodness of the taste, we did want to include it to some extent. Therefore, we decided to make a combination of something random (and independent of the ingredient) and the rating. For the random criterium, we opted for the number of consonants in an ingredient. This comes down to a fitness function of 0.1 * rating + 0.9 * n_consonants (exl. the binary criteria).

Secondly, some recipes from the inspiring set did not have a rating. We solved this by adding our own rating, based on our own liking of the ingredients. Another problem with the recipes from the inspring set was the ingredients were measured in different units (e.g., cups, ounces, and grams). To achieve a recipe that takes into account a correct ratio of the ingredients, we converted all the units to grams and ml by using the library Sugarcube. This library already contained the density of the products water, sugar, flour, butter, and salt, therefore these ingredients were automatically converted. For the density of other ingredients, we categorised them in classes, such as liquid for milks and sauces, and gave them a general density based on information online. After catergorising all the ingredients, we added their densities to the library, whereafter the units were converted. 


### Presentation
When we were first talking about creating mochi, we also quickly came up with how we wanted to present it. Since mochi is originally from Japan, we wanted to give our cookbook a Japanese theme: the title of the cookbook and the recipe names would be written in Japanese signs, we would add some cute "kawaii" mochi of our recipes, and we limited ourselves to soft pastel colours usually associated with this "kawaii" drawing style. We hand designed the cookbook. We decided that we wanted to create a tiny pocket cookbook as that would make it instantly cute and that would fit well within our mochi theme. 
We used generative AI to create fitting titles for the mochi recipes and to create a kawaii cartoon style version of the generated recipe.

We hand-designed the cookbook and used placeholders for the ingredients, instructions and images of the generated recipe.

At some point we realised that by adding our list of random ingredients, we would essentially be creating monsterous mochi. This sounded quite nice to us and resulted in the renaming of our project from "Cookie monsters" to "Mochi monsters".

[Whatever way you produce your cookbook, think about the presentation of your recipe as part of the larger "creative system", as a way of increasing the perceived value of a recipe by "persuading" a potential cook that it would be good to try.]

https://www.canva.com/design/DAGUYibnRzg/cqlxfxbQ7bQ5u21EhB991g/edit?utm_content=DAGUYibnRzg&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

We hand-designed the cookbook and used placeholders for the ingredients, instructions and images of the generated recipe.

## Reflection on the question of how to evaluate the creativity of your system 


Your logbook should note which parts of the cookbook were generated using a Generative AI.!!!


#### Puntjes waar we tegenaan liepen:
amounts:
- pinch of
- whole as a unit (a whole egg)
- dust the surface

## TO DO
1. inspiring set recipe list
    - Ieder van ons voegt gekke ingredienten toe en rate deze
    - Rate ook de onreviewde recepten
    - Alles omzetten naar grammen (de hele ingredientenlijst via chatgpt omzetten)
    - lijst maken van alle noten die bestaan, als het een noot is class "nuts" toevoegen (hazelnoot, pistache, cashew, pecan, )
    - gluten


2. de fitness criterium/evaluation (Linthe)
    - (0.9 * n_consonants + 0.1 * rating)
        * presence_flour (dat is 1 of 0)
        * presence_egg
        * presence_nuts
        * presence_bakingpowder
        * gluten ()

        (last four are binary)

        - dus hvh consonants berekenen per ingredient
            - is het gemiddeld hvh medeklinkers (tot / n_ingredients)
        - rating per ingredient
        - summen van alle consonants en mean rating van alle ingredienten
        - doesn't take ingredients containing gluten + nuts
        - important that it includes flour
            - 1 if flour = 1 and 0 if flour <1 OR flour > 1
        - recipes for 10 servings of mochi

        wat is belangrijk voor mochi: dat het goede verhouding water/flour heeft en een filling.

    - er moeten basis ingredienten in zitten (bv de flour) voor het deeg
    - alles wat niet-deeg is automatisch filling of topping.

    - crossover functie kiezen (zelfde als voorbeeld)

    - bedenken hoe we willen muteren (Emma nadenken) (hier komen de losse ingredienten)
        - substitute (only substitute ingredients with same unit bv cup not substituted with tablespoons) -> dit zorgt ervoor dat het misschien de goede verhoudingen behoudt MAARR haalt wel misschien "novelty" weg. Hopelijk voegen we dat toe met die random ingredienten als ze reageren op bs.
        - adding random ingredient from our list
        - removing ingredient
        - 

    2.2 general outline code json bestand maken met 2 lijsten (Emma)
    
3. standaard recept (template) met invul variabelen (Sanne)

4. using genAI for presentation (Sanne / allen)
https://lingojam.com/JapaneseText
Alles kawaii en cutie

- eigenlijk al het kookboek maken met placeholders (Emma)

5. logboek schrijven (Emma)

6. nadenken over evaluatie van onze creativiteit systeem ()
- weer met iemand laten uitproberen?
- lovelace 2.0 test


