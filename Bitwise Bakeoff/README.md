# MochiMonsters Recipe Generator 
This project generates Mochi recipes using 40 mochi recipes from [this](https://allpurposeveggies.com/12967/12-mochi-flavors-easy-recipes-for-mochi-ice-cream-and-more/) and [this website](https://thericechick.com/mochi-recipes/). Additionally, it uses 29 loose ingredients to vary the output some more. With webscraping and this additional ingredients it will compose the inspiring set and with using an evolutionary algorithm it will generate a Mochi recipe based on ratings higher than 4.6, including 5-8 ingredients, glutenfree, and nutfree.

**Contributions**   
MochiMonsters Recipe Generator is created by Emma Boom, Sanne Dekker and Linthe van Rooij. 

## Prerequisites
### Libraries
- Webscraping and preprocessing: 
    - bs4: BeautifulSoup for scraping
    - sugarcube for transforming proportions 
    - re and string: for formatting 
    - json: for saving and reading files 
- Making the recipes:
    - pprint: for pretty JSON structure display
    - math and random: for calculations

### Structure of the directory
- data/
    - mochi.json
    - weird_ingredients_list.json
- recipes_output/
    - .txt files of generated recipes
- 1 preprocessing.ipynb
- 2 main.ipynb
- Logbook.md
- README.md


## Run the code! 
1. Make sure to have all necessary libraries installed. 
2. This code is written in Jupyter Notebook, make sure to have all necessary components installed for this. 
3. RUN ALL CELLS in 2 main.ipynb
4. This will create a freshly generated recipe in the "recipes_output" folder. 




