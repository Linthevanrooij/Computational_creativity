# Log file of Computational Creativity Bitwise Bakeoff

## Initial Idea  
Our initial idea for the Bitwise Bakeoff is to create a mochi recipe generator. Mochi is a traditional Japanese food made from glutinous rice, known as mochigome in Japanese. This soft, chewy dough forms a rice cake that can be wrapped around various fillings. There are many variations of mochi, as it can be filled with ingredients like red bean paste or ice cream. Mochi flavours can be both sweet and savoury. Because of this flavour variety, we thought mochi would be the perfect food to inspire a recipe generator.

We plan to use these websites for our initial set of inspiring recipes:
https://allpurposeveggies.com/12967/12-mochi-flavors-easy-recipes-for-mochi-ice-cream-and-more/
https://thericechick.com/mochi-recipes/

Additionally, to generate unique and unusual mochi flavours, we plan to create our own list of inspiring ingredients to combine with mochi. To calculate the fitness of each ingredient, from both the external recipe sources and our own list, we will use the ratings (1 to 5 stars) from the existing recipes. For each ingredient found in a recipe, we will assign it the recipe’s rating. If an ingredient appears multiple times, we will use the average rating. For ingredients from our own list, we will rate them ourselves and calculate the average score based on the three of us.

For the presentation of our recipes, we like to maintain the Japanese style. Therefore, we plan to use a text generator that creates Japanese-like symbols from standard text, and use this for the instructions and ingredient list of the recicpe (https://lingojam.com/JapaneseText). Another idea is to present the recipes in a kawaii style. Kawaii is a part of Japanese culture that emphasizes cuteness. We can achieve this by creating AI-generated images of cute mochi designs that match the ingredients in the recipe.

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

Your logbook should note which parts of the cookbook were generated using a Generative AI.

## Updates on idea/new goals


## Step-by-step account on how to tackled tasks (inspiring set, implement recipe generator, presentation) + reflection on development

Presentation:
https://www.canva.com/design/DAGUYibnRzg/cqlxfxbQ7bQ5u21EhB991g/edit?utm_content=DAGUYibnRzg&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

We hand-designed the cookbook and used placeholders for the ingredients, instructions and images of the generated recipe.

### Limitations

#### Puntjes waar we tegenaan liepen:
- ingredienten waren in verschillende maten (bv cup en oz en grammen), dus die moesten we omzetten.
- hoe bepaal de je rating van recepten die geen rating hebben
    - mogelijkheden: zelf raten (probleem: wij bepalen de fitness, bias), gemiddelde nemen van alle recept ratings (probleem: dan gaat het niet om rating van dit specifieke recept), 
- add rating to individual ingredients so that fitting fits.

- We were not sure if using simply the rating would result in new recipes, since an evolution algorithm would then just give recipes with the highest rated ingredients, and the non-rated and lower rated ingredients would not stand a chance. Therefore, we started looking into other fitness criteria. We thought about the ingredient being vegan/vegetarian/gluten-free or cooking time.
We argued that we needed to find a criterium that has nothing to do with the quality of the ingredient itself (such as length of ingredients in the example code). But since a rating of a recipe (and thus an ingredient) does possibly say something about the goodness of the taste, we did want to include it to some extent. Therefore, we decided to make a combination of something random (and independent of the ingredient) and the rating. For the random criterium, we opted for the number of consonants in an ingredient. This comes down to a fitness function of 0.1 * rating + 0.9 * n_consonants.

Now: 0.1 * rating + 0.9 * n_consonants

Er zit wat subjectiviteit in van onze rating.

amounts:
- pinch of
- whole as a unit (a whole egg)
- dust the surface


## Reflect on experience of generative AI


## Reflection on the question of how to evaluate the creativity of your system 