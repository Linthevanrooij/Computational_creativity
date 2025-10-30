# Instructions

In this project assignment you are required to build a recipe generator for cookies and/or cakes using an approach similar to the one explored in Homework Assignment 5: Simple PIERRE.

## Assignment Subtasks
The assignment task can be broken down into the following subtasks:

### Gather an Inspiring Set for Cookie/Cake Recipes
Keep in mind that you will want to be able to combine elements of different recipes to produce novel (and delicious) recipes but this doesn't mean that you need to limit yourself to only sweet recipes. For example, you might want to include savoury muffin recipes in an inspiring set for cakes to provide your system with the potential for interesting ingredient combinations.

Homework Assignment 5 used a very small inspiring set, by contrast the PIERRE system on which the homework assignment was based had 5,000 recipes! You don't need to gather that many recipes but also probably want more than the few recipes used in Simple PIERRE. To get you started, here are some links to some basic cookie dough recipes:
- Easy Sugar Cookies
- Oatmeal Cookies
- Chocolate Cookie Dough
- Crazy Cookie Dough
- Shortbread

You will notice that many of these cookie recipes follow the same general instructions, with just a few differences in terms of what is added. Keep this in  mind when you think about the presentation of your recipes. You don't have to use these recipes for your inspiring set, they have been provided to give you a starting point, there are plenty of recipe sites online. You might also want to check out Wikipedia's List of Notable Cookies for more inspiration.

You are also NOT limited to having an inspiring set of recipes, remember that according to Ritchie the inspiring set can be implicitly defined by the knowledge that the developer has about examples from the creative domain. In this context, this could mean that you choose to gather together a list of suitable ingredients with meta-level information (perhaps coded into the genetic algorithm) about how ingredients might be combined.

### Create a Knowledgebase for the Inspiring Set
This knowledgebase could take the form of a JSON file, as used in Homework Assignment 5, but you can use whatever system you would prefer. You might want to think about what tool would help you gather the recipes most easily and then convert the result of this into a form that is easy for a computational system to read.

Think carefully about the information you want to capture in your inspiring set knowledgebase. The JSON file used in Homework Assignment 5 does not represent everything that you might want to know about a recipe or an ingredient. For example, you might want to record broad classes of recipes if you want to include more than one type of recipe in your inspiring set, e.g., cake, cookie, biscuit, muffin, savoury muffin, or possibly the meal time most appropriate for a recipe, e.g., breakfast, snack, desert. You might also want to including information about different classes of ingredients used in recipes, e.g., sweet, savoury, liquid, herb, spice, etc., or the role that an ingredient plays, e.g., binding agent, rising agent, seasoning, decoration, etc. Obviously, it only makes sense to spend the time adding this information if you think you can use these classifications to generate and/or evaluate recipes more intelligently.

### Implement a Recipe Generator using a Genetic Algorithm
Implement a genetic algorithm that is able to use the inspiring set database to evolve populations of cookie/cake recipes. This could be based on the code provided for Homework Assignment 5, or you can implement your own system in whatever programming language you prefer, e.g., Python.

You may use external libraries to implement the mechanics of the genetic algorithm itself. For example, you might consider using the geneticalgorithm library for Python, which provides an easy way to implement a simple genetic algorithm but also imposes some limitations that you may have to consider, e.g., it assumes a fixed length genotypes of numbers (how might you rethink how to encode a recipe within this type of scheme?).

Whichever way you go with the implementation, think about the stopping criteria for your genetic algorithm and what you want your system to output at the end of a run, e.g., should your system run for a fixed number of generations and return the best recipe found so far, or should its run be controlled interactively by a user.

### Present Generated Recipes in a Small Cookbook
Decide how you want to present the recipes that your system has generated in a small cookbook. As with Assignment 1, use a Generative AI to help you present your recipes, e.g., to produce illustrations or provide a backstory for the recipe (or chef). To produce your cookbook you can use any tool that will allow you to format your recipe, e.g., Word, Photoshop, etc. You are NOT expected to generate your cookbook as part of your generative system but you can if you want to. You are encouraged to use Generative AI systems, as you did for Assignment 1, to illustrate and/or embellish your cookbook, e.g, images of what your cookies might look like or perhaps inventing a story behind your recipes, or the chef.

Whatever way you produce your cookbook, think about the presentation of your recipe as part of the larger "creative system", as a way of increasing the perceived value of a recipe by "persuading" a potential cook that it would be good to try. This might include adding instructions for how to cook the cookie/cake, or you might want to try to devise a template with placeholders for the names of ingredients used in the recipe (e.g. using techniques from Assignment 1). You might also want to consider what other features of a cookbook recipe help to persuade.

## Deliverables
The deliverables for this assignment are:

1. A file (e.g. a PDF or Jupyter notebook) containing a "logbook" of your process and reflections on developing your creative system, which provides a brief step-by-step account of how you tackled the tasks outlined above and your thoughts on the process, e.g., how you decided on your inspiring set. The final entry of you logbook should be a reflection on the question of how to evaluate the creativity of your system, or if you tried to conduct an evaluation how this went.
2. A zip source code and data files for your creative system. This should include a README file that describes the system requirements for compiling and running your system. NOTE: If you develop your system using the online editor at P5js you should download a copy of your source files and submit this.
3. A file (e.g. a PDF or webpage) containing your small "cookbook" of at least three examples of the recipes generated by your system. (Your logbook should note which parts of the cookbook were generated using a Generative AI.)

Due on 28 October 2024 23:59