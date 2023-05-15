# Japanese-to-English-Translator
This is a translator program I built using Python that will take in a sentence in Japanese and translate the parts of the sentence into English and return an English translation.

The original senetence is first split into various parts of speech using Japanese particles, which determines the transitivity of the verb if present and if a copula is present. Each part of speech is further broken down depending on the characters, length, conjugation, pairing, and use.

This program does utilise the googletrans library as making a translator is a near impossible task (even for Google), especially without the use of machine learning.

The main feature of the program is to take the individual parts of the sentence, translate it using a csv with common words in Japanese, match it to a part of speech in English, and return that to the user.

The files in the program are as follows:
  BasicWords.py -> Has multiple dictionaries and lists with conjugations, copulas, translations, adverbs, and adjectives
  CleanCommonDataset.ipynb -> Used to take the original, messy dataset of common Japanese words and clean it using Jupyter Notebooks
  common_japanese.csv -> A csv file cleaned from the original file that has japanese words along with their definitions and readings
  CreateJLPTDeck.py -> Used to scrape the jisho.org website and download the common dataset used in this program
  GoogleTranslate.py -> Used to translate the sentence from the user into English semi-accurately
  Main.py -> Main file for the program that initializes everything and calls all of the methods and variables
  Translate.py -> Stores various methods to help with the main method. Used extensively
  
 Examples of the program with Japanese inputs:
  Transitive Sentences:
    With を and は: 
    ![image](https://github.com/ashsProjects/Japanese-to-English-Translator/assets/101825086/d66b5b81-b86a-4b19-af81-0df85610bd74)
    With する verb: 
    ![image](https://github.com/ashsProjects/Japanese-to-English-Translator/assets/101825086/808cdbe5-424f-45eb-b899-b5ca7de9e22d)
    With modifier in subject: 
    ![image](https://github.com/ashsProjects/Japanese-to-English-Translator/assets/101825086/0d175f06-88e1-4a56-82f1-ffbd69e9683d)
    With modifier in object: 
    ![image](https://github.com/ashsProjects/Japanese-to-English-Translator/assets/101825086/3fbe730a-d284-4404-8f1d-fc725d5c142f)
    With の in subject: 
    ![image](https://github.com/ashsProjects/Japanese-to-English-Translator/assets/101825086/5daa4eb6-e384-45b9-b1db-3390177ec2ac)
  Intransitive:
    With は and に: 
    ![image](https://github.com/ashsProjects/Japanese-to-English-Translator/assets/101825086/b070aa6a-d67e-4bcd-b8c0-87ce409d6fd6)
    With いる and に: 
    ![image](https://github.com/ashsProjects/Japanese-to-English-Translator/assets/101825086/207ad27f-66bc-4aa5-8101-2f426eea7d8f)
    With 行く and に: 
    ![image](https://github.com/ashsProjects/Japanese-to-English-Translator/assets/101825086/cf6a3ac3-161b-4848-906d-3cd9fcae1ba9)
    With modifier in location and に: 
    ![image](https://github.com/ashsProjects/Japanese-to-English-Translator/assets/101825086/9f65c9ce-c43b-4d45-86a4-34b37b1e8e6a)
    With の in location　and に 
    ![image](https://github.com/ashsProjects/Japanese-to-English-Translator/assets/101825086/7a865682-f4b6-4eee-85b9-beff03b87502)
    With は and が: 
    ![image](https://github.com/ashsProjects/Japanese-to-English-Translator/assets/101825086/d19c6f29-45f4-479d-9095-9210fde83389)
    With が and ある: 
    ![image](https://github.com/ashsProjects/Japanese-to-English-Translator/assets/101825086/f445f3b6-3173-4257-97f1-23fb8542c198)
    With modifier in object　and が: 
    ![image](https://github.com/ashsProjects/Japanese-to-English-Translator/assets/101825086/68644d71-b652-41a7-bdf7-689a75cc97f2)
    With の in subject　and が: 
    ![image](https://github.com/ashsProjects/Japanese-to-English-Translator/assets/101825086/8ea30a5c-da70-42fa-8610-f294d085270b)
  Copula:
    With は: 
    ![image](https://github.com/ashsProjects/Japanese-to-English-Translator/assets/101825086/9e580390-8f5d-4821-a188-3c3c367b90e4)
    With が: 
    ![image](https://github.com/ashsProjects/Japanese-to-English-Translator/assets/101825086/174461ac-ca99-4e0a-a86a-45b35f876dac)
    With い-adjective: 
    ![image](https://github.com/ashsProjects/Japanese-to-English-Translator/assets/101825086/2a19409f-be9b-4dfe-8d7f-b43a34a2c6e9)
    With な-adjective: 
    ![image](https://github.com/ashsProjects/Japanese-to-English-Translator/assets/101825086/c2510d37-0d5c-4c3e-8eeb-c61ec0264589)
    With modifier in object: 
    ![image](https://github.com/ashsProjects/Japanese-to-English-Translator/assets/101825086/a203a088-2814-4b61-8fe9-3c6c2f707e63)
    With の in subject: 
    ![image](https://github.com/ashsProjects/Japanese-to-English-Translator/assets/101825086/68106cb4-585b-46c2-9056-83f57aeaf1a9)

These are just few examples of the translations. The program has its limitations as it only supports 5-6 particles and fairly basic N5 grammar. I hope to continue building onto the program.
