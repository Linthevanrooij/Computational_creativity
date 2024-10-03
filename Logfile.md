# Log file of Computational Creativity Poem Generator 

## Initial Idea of poetry generator
25/09/2024

As inspiring set of the poem generator we chose rap lyrics. Rap lyrics in general is being said to be poetic. To not mix different styles, we chose to only select the lyrics of one artist to be included in the data set. For the artist we chose one to be known as one of the most poetic rap artist in general: JCole ([Rap poets](https://medium.com/writers-daily/why-poets-should-be-like-rappers-0b21a8bdff77#:~:text=Myriad%20rappers%20have%20been%20called,poets%20and%20the%20new%20rappers)). We began with a dataset of only one song to start simple, we chose his best known song: Lights Please. The final idea is to make the generator based on different songs of JCole.

As for the implementation of poem generator, we first explored the different available techniques (grammar, templates, markov chains) and from there, chose one that suits are project the best. For the format we want to use an "elfje", which is similar like a Didactic cinquain. This is a structure composed of 5 lines in which the first line includes 1 word, the second 2 words, the third 3 words, the fourth 4 words, the fifth 1 words again. Predefined rules on these lines can be found on http://www.poezie-in-beweging.nl/framerechts/poezie_en_opdrachten/maakeeneigengedicht/elfje.html

To present our poems we, want to use an generative AI that produces text-to-speech in a rap format ([GenerativeAI](https://www.topmediai.com/app/text-to-speech/?voice=67ade205-5d4b-11ee-a861-00163e2ac61b)), rapped by JCole/Kendrick itself! And maybe we want to include a beat in the final record. 

## Updates on idea/new goals
03/10/2024

For the presentation, we have an idea of integrating both audio functionality and visual elements that simulate an audio player interface resembling a platform like Spotify. This will give the appearance that the audio sample is part of an album by J. Cole. We plan to use PowerPoint to design this audio player because this allows us to not only mimic an audio player interface but also play the actual sound sample. Additionally, we can use generative AI tools to create a custom album cover image to create a combination of J. Cole’s style and the poem's style.

## Step-by-step account on how to tackled tasks (inspiring set, implement poem generator, presentation) + thoughts
03/10/2024

We chose to use grammars for our poem generator, similar to the grammar used in the haiku generator. We believed this approach would be most effective since there are structural similarities between a haiku and an elfje. Both poetic forms follow strict, predetermined patterns. In the case of the elfje, it adheres to a structure of eleven words distributed across five lines. This allowed us to define and maintain the specific word count and layout required for the elfje format. For our elfje, we set up a text file and started with a production rule of five lines. The non-terminal symbols can be defined after analyzing the rap lyrics.

To analyse the rap lyrics, we used the RiTa library. We began by analyzing J. Cole's song "Lights Please" to simplify the process and work with a more manageable set of lyrics. We used the rita.tokenize() function to split the lyrics into individual tokens, which made it easier to analyse the structure and content of the lyrics. We used the rita.pos() function to tag each word with its corresponding part of speech (POS). With these tags, we were able to define the non-terminal symbols and set up the production rules of the elfje. This was done according to the following rules:

Line 1: 	one word: a characteristic (adjective).

Line 2: 	two words: an object or person (noun / pronoun).

Line 3: 	three words: start this line with a noun, followed by a verb. These three words provide further explanation of
            the object or person.

Line 4: 	four words: start this line with ‘I’. In this line, your relation to the object or person is described.

Line 5: 	one word: closing word

After setting up all production rules, we successfully ran the poem generator. Next, we could easily add other lyrics, by tokenizing, tagging, and incorporating them into the text file.


## Process and reflections on development

reflection on analyzing lyrics





The large variety of part-of-speech tags made setting up the production rules more complex than initially expected. For example, ensuring that the elfje was grammatically correct required matching the appropriate type of verb with the corresponding pronoun. This resulted in numerous potential tag combinations for the production rules. Another challenge we faced was deciding which specific tags to use within each line of the elfje to maintain both the poem's structure and grammatical accuracy. Although we resolved these issues, the generated poems still lack linguistic correctness sometimes. However, we realized that many rappers often rap without strict adherence to grammatical rules, so whenever our poems are linguistically incorrect, it could be argued that this aligns more closely with the rap theme.


## Reflect on experience of generative AI

## Reflection on the question of how to evaluate the creativity of your system 

