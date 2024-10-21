# Log file of Computational Creativity Bitwise Bakeoff

## Initial Idea 
Mochi!!! 


## TO DO
1. inspiring set recipe list
    - Ieder van ons voegt gekke ingredienten toe en rate deze
    - Rate ook de onreviewde recepten
    - Alles omzetten naar grammen (de hele ingredientenlijst via chatgpt omzetten)


2. de fitness criterium/evaluation
    - 0.9 * n_consonants + 0.1 * rating
        - dus hvh consonants berekenen per ingredient
        - rating per ingredient
        - summen van alle consonants en mean rating van alle ingredienten
        - doesn't take ingredients containing gluten + nuts

    - er moeten basis ingredienten in zitten (bv de flour) voor het deeg
    - dough heeft 
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



## Updates on idea/new goals


## Step-by-step account on how to tackled tasks (inspiring set, implement recipe generator, presentation) + reflection on development


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


## Reflect on experience of generative AI


## Reflection on the question of how to evaluate the creativity of your system 