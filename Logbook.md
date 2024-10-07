# Log file of Computational Creativity Poem Generator by Linthe van Rooij en Sanne Dekker

## Initial Idea of poetry generator
_25/09/2024_

As an inspiring set of the poem generator, we chose rap lyrics. Rap is sometimes associated as an acronym for ['Rhythm And Poetry'](https://www.musicianwave.com/does-rap-stand-for-rhythm-and-poetry/), although the origin of 'rap' stems from a different definition, it is not misplaced. Often, the rap that is written does have deeper layers of meaning, which is therefore a perfect inspiring set for this assignment. We chose to stick to songs of only one artist since there are a lot of different styles in rap. As an artist we chose one to be known as one of the most poetic rap artists in general: J. Cole ([Rap poets](https://medium.com/writers-daily/why-poets-should-be-like-rappers-0b21a8bdff77#:~:text=Myriad%20rappers%20have%20been%20called,poets%20and%20the%20new%20rappers)). We began with a dataset of only one song to start the coding simple, we chose one of his best-known songs: Lights Please. The final idea is to make the generator based on different songs from J. Cole.

As for the implementation of the poem generator, we first explored the different available techniques (grammar, templates, Markov chains) and from there, chose one that suited our project the best. For the format, we want to use an "elfje", similar to a Didactic cinquain. This structure is composed of 5 lines, the first line includes 1 word, the second 2 words, the third 3 words, the fourth 4 words, and the fifth 1 word again. Predefined rules on these lines can be found [here](http://www.poezie-in-beweging.nl/framerechts/poezie_en_opdrachten/maakeeneigengedicht/elfje.htm0l). 

To present our poems we want to use a generative AI that produces text-to-speech in a rap format ([GenerativeAI](https://www.topmediai.com/app/text-to-speech/?voice=67ade205-5d4b-11ee-a861-00163e2ac61b)), rapped by the voice of J. Cole himself. And maybe we want to include a beat in the final record. 

## Updates on idea/new goals
_03/10/2024_

For the presentation, we have an additional idea of integrating both audio functionality and visual elements that simulate an audio player interface resembling a platform like Spotify. This will give the appearance that the audio sample is part of a new "poetry album" by J. Cole. We plan to use PowerPoint to design this audio player because this allows us to not only mimic an audio player interface but also play the actual sound sample. Additionally, we can use other generative AI tools to create a custom album cover image to create a combination of J. Cole’s style and the poem's style.

_05/10/2024_

Since powerpoint is still limited with the notation of audio, we found that our desinging platform Canva also allows transitions and audio as part of the design. We therefore changed the presentation style to a video containing all necessary elements, to simulate the experience of listening to the new released poems. 

## Step-by-step account on how to tackled tasks (inspiring set, implement poem generator, presentation) + reflection on development
_03/10/2024_

We chose to use grammars for our poem generator, similar to the grammar used in the haiku generator. We believed this approach would be most effective since there are structural similarities between a haiku and an elfje. Both poetic forms follow strict, predetermined patterns. In the case of the elfje, it adheres to a structure of eleven words distributed across five lines. This allowed us to define and maintain the specific word count and layout required for the elfje format. For our elfje, we set up a text file and started with a production rule of five lines. The non-terminal symbols can be defined after analyzing the rap lyrics.

To analyse the rap lyrics, we used the RiTa library. We began by analyzing J. Cole's song "Lights Please" to simplify the process and work with a more manageable set of lyrics. We first used the rita.tokenize() function to split the lyrics into individual tokens, which made it easier to analyse the structure and content of the lyrics. However, since a lot of verbs contained quotation marks as part of the word (for example: bein'), we had to use the build-in split method of Javascript to gain a better method in splitting because we wanted to keep this style of speech in the final poems. We used the rita.getPosTags() function to tag each word with its corresponding part of speech (POS). We had to redefine some of the verbs with quotation marks, since these were tagged incorrect as nouns. With the final tags, we were able to define the non-terminal symbols and set up the production rules of the elfje. This was done according to the following rules:

- Line 1: 	one word: a characteristic (adjective).
- Line 2: 	two words: an object or person (noun / pronoun).
- Line 3: 	three words: start this line with a noun, followed by a verb. These three words provide further explanation of
            the object or person.
- Line 4: 	four words: start this line with ‘I’. In this line, your relation to the object or person is described.
- Line 5: 	one word: closing word

The large variety of part-of-speech tags made setting up the production rules more complex than initially expected. For example, ensuring that the elfje was grammatically correct required matching the appropriate type of verb with the corresponding pronoun. This resulted in numerous potential tag combinations for the production rules. Another challenge we faced was deciding which specific tags to use within each line of the elfje to maintain both the poem's structure and grammatical accuracy. Although we resolved these issues, the generated poems still lack linguistic correctness sometimes. However, we realized that many rappers often rap without strict adherence to grammatical rules, so whenever our poems are linguistically incorrect, it could be argued that this aligns more closely with the rap theme.

After completing the production rules, we successfully ran the poem generator. Now, we could easily add other lyrics, by tokenizing/splitting, tagging, and incorporating them into the final grammar sheet. In total, we added three songs of J. Cole: [Lights Please](https://songteksten.net/lyric/8029/95243/j-cole/lights-please.html), [No Role Modelz](https://lyrics.lyricfind.com/lyrics/j-cole-no-role-modelz), and [Middle Child](https://lyrics.lyricfind.com/lyrics/j-cole-middle-child). We selected four generated poems for our presentation.

_04/10/2024_

Next, we started working on the presentation. To visualize an audio player, we chose to use Canva instead of PowerPoint, since Canva is a design tool that allowed us to easily create a mock-up of a phone screen with a Spotify-like interface. The audio for the presentation was generated using two programs: TopMediai (https://www.topmediai.com/app/text-to-speech/) was used to produce the speech and generate J. Cole's voice for the poems that we selected; Tuney (https://app.tuney.io/) was used to add a beat behind the generated speech. Additionally, we used an text-to-image generator (https://www.imagine.art/dashboard/tool/text-to-image) to create custom album covers based on the text of the poems.


## Reflect on experience of generative AI
_04/10/2024_

Working with three different AI programs considerably expanded the creative possibilities for presenting our poems. It was also surprising to realize just how much is possible with all the AI programs that are available today. For instance, the text-to-speech generator provided a wide selection of voices, which we could further customize by adjusting the speed, volume, pronunciation, and pitch. The beat generator also offered an extensive range of options, producing an endless supply of beats across various genres. For our project, we specifically chose beats from the hip-hop and R&B genres. As for the image generator, there were also numerous options available to generate images in a variety of styles.

We think the use of generative AI significantly elevated the output of our poem generator. Because the poems sometimes lacked perfect coherence, having a voice like J. Cole narrate them gave the poems a more realistic, rap-like feel, just as the real songs produced by J. Cole. Hearing the poems spoken aloud made them feel more like rap lines rather than disjointed text on a page. The addition of a beat further enhanced this effect, and made the poems more rhythmic. The AI-generated album covers also contributed to the overall presentation, because it added a fun and creative element to the audio interface mock-up.


## Reflection on the question of how to evaluate the creativity of your system 
_06/10/2024_

Based on [Ritchies Empirical Criteria](https://link.springer.com/article/10.1007/s11023-007-9066-2), we could attribute the creativity of our system. According to these criteria, we could judge the artifact based on:
- typicality
- novelty
- quality

1. Typicality

This addresses whether the produced output is a recognizable example of the target genre. In our case, if the produced Elfje is still to be recognized as the same style as JCole. Since we did not change any of the type of wording (keeping existin' the same instead of making it correct), the system included this in the poems as well, keeping the style of language more or less the same. Also, the choice of presentation style attributed a lot to the typicality. With the rhythmic style of the Elfje, it kept the same rhythmic style as normal in this genre. Adding a beat to the output of speech and creating a novel image as covers contributed to the recognizability of the output in the same context as normal songs. 

2. Novelty

With novelty, it is evaluated how dissimilar the produced output is from the inspiring set (our three chosen songs) within the context of the style of JCole. Since we used three different songs there are a lot of different combinations that the system could choose from. Within these combinations, there are existing themes like light and bright but within a whole different context, i.e. lights being proud and making the king bright instead of the darkness as in the original song. With these new combinations, you are going to search for meaning within the poems, making them novel and able to stand alone, apart from the original meaning behind the words in the songtexts. Although there are not completely novel words in the poem itself, the combination and meaning of words is novel. Moreover, the produced speech and album covers are novel to the system, as they are not present in the inspiring set. 

3. Quality

Quality addresses the value of the artifact as an example of the target genre. In other words, are the produced Elfjes still grammatically correct, given the style of rap, are they coherent and are they saying something? In the selected poems, as said before, you as the reader or listener are going to search for meaning behind the words. And given the fact that the style is not 100% grammatically correct (just as rap itself), it still has a lot of coherence (light/ bright or a mad toothbrush, selling it fast) and even rhyme (mad toothbrush had). 

We asked the following questions to someone who is an expert with rap and JCole's music. With output, we mean the textual output of our system, in other words, the generated Elfjes. 

1 (completely disagree) - 5 (completely agree)
- I recognize the style of JCole 3
- Would you say the output created some novel content? 4
- Is the output novel while adhering to the context of JCole? 4
- I find the output coherent (given the style of rap) 5
- I can find some meaning behind the output 3
- I think the output is creative 5

As shown in these evaluation results, the overall rating is 24/30. The overall creativity is rated as high as possible (5/5). When we look at the individual categories defined by Ritchie, quality, and novelty are rated the highest, while typicality is rated a bit lower. This short evaluation indicates that our system can create novel output with a high value, while still adhering to the style of JCole (3/5). 
