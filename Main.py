import Translate
import GoogleTranslate
import BasicWords

def get_input_from_user() -> str:
    """A method to get an input from the user.
    \nReturns a str with the user's input"""
    return input("Enter your sentence to be translated (enter x to exit): \n")

def process_transitive(sentence: str) -> None:
    """A method to process the sentence if a "を" is in the sentence, denoting that it is a transitive.
    Splits the sentence based on particles and modifiers using methods imported from the Translate module.
    \nEvery part of speech that is not empty if added to the POS dictionary and passed into the 
    translate_and_print() method."""
    subject = []
    direct_object = []
    verb = []
    verb_ending = ""
    modifier = []
    POS = {}
    
    verb_phrase_list = Translate.strip_hiragana(sentence[sentence.index("を") + 1:])
    if len(verb_phrase_list[0]) != 0: verb.append(verb_phrase_list[0])
    verb_ending = "" if len(verb_phrase_list[1]) == 0 else verb_phrase_list[1]
    
    sentence_until_wo = Translate.split_by_particle(sentence[:sentence.index("を")])
    
    object_phrase = sentence_until_wo[-1]
    if len(object_phrase) >= 3:
        split_modifier = Translate.find_modifiers(object_phrase)
        if len(split_modifier) >= 2:
            modifier.append(split_modifier[0])
            object_phrase = split_modifier[1]
    if "の" in object_phrase:
        split_by_no = Translate.split_no(object_phrase)
        #Adding the subject phrase at position 0, the word before no at 1, and the word after at 2
        direct_object.append(object_phrase)
        direct_object.append(split_by_no[0])
        direct_object.append(split_by_no[1])
    else: direct_object.append(object_phrase)
    
    subject_phrase = ""
    if "は" not in sentence_until_wo:
        if "が" not in sentence_until_wo:
            subject_phrase = "私"
        else: subject_phrase = sentence[:sentence.index("が")]
    else: subject_phrase = sentence[:sentence.index("は")] 
    
    if len(subject_phrase) >= 3:
        split_modifier = Translate.find_modifiers(subject_phrase)
        if len(split_modifier) >= 2:
            modifier.append(split_modifier[0])
            subject_phrase = split_modifier[1]

    if "の" in subject_phrase:
        split_by_no = Translate.split_no(subject_phrase)
        #Adding the subject phrase at position 0, the word before no at 1, and the word after at 2
        subject.append(subject_phrase)
        subject.append(split_by_no[0])
        subject.append(split_by_no[1])
    else: subject.append(subject_phrase)
    
    POS.update({"Subject": subject})
    if len(verb) > 0: POS.update({"Verb": verb})
    POS.update({"Verb Ending": verb_ending})
    POS.update({"Object":direct_object})
    if len(modifier) > 0: POS.update({"Adverbs": modifier})
    
    translate_and_print(POS)
        
def process_copula(sentence: str) -> dict:
    """A method to process the sentence if a copula is in the sentence.
    Splits the sentence based on particles and modifiers using methods imported from the Translate module.
    \nEvery part of speech that is not empty if added to the POS dictionary and passed into the 
    translate_and_print() method."""
    subject = []
    noun_modifier = []
    copula = ""
    modifier = []
    POS = {}
    
    copula_list = Translate.find_coupla(sentence)
    split_list = Translate.split_by_particle(copula_list[0])
    
    copula = copula_list[1]
    split_list.append(copula)
    
    subject_phrase = ""
    if "は" not in split_list:
        if "が" not in split_list:
            subject_phrase = "私"
        else: subject_phrase = split_list[split_list.index("が") - 1]
    else: subject_phrase = split_list[split_list.index("は") - 1]
    
    if len(subject_phrase) >= 3:
        split_modifier = Translate.find_modifiers(subject_phrase)
        if len(split_modifier) >= 2:
            modifier.append(split_modifier[0])
            subject_phrase = split_modifier[1]

    if "の" in subject_phrase:
        split_by_no = Translate.split_no(subject_phrase)
        #Adding the subject phrase at position 0, the word before no at 1, and the word after at 2
        subject.append(subject_phrase)
        subject.append(split_by_no[0])
        subject.append(split_by_no[1])
    else: subject.append(subject_phrase)
    
    noun_modifier_phrase = split_list[split_list.index(copula) - 1]
    if len(noun_modifier_phrase) >= 3:
        split_modifier = Translate.find_modifiers(noun_modifier_phrase)
        if len(split_modifier) >= 2:
            modifier.append(split_modifier[0])
            noun_modifier_phrase = split_modifier[1]
    if "の" in noun_modifier_phrase:
        split_by_no = Translate.split_no(noun_modifier_phrase)
        #Adding the subject phrase at position 0, the word before no at 1, and the word after at 2
        noun_modifier.append(noun_modifier_phrase)
        noun_modifier.append(split_by_no[0])
        noun_modifier.append(split_by_no[1])
    else: noun_modifier.append(noun_modifier_phrase)
    
    POS.update({"Subject": subject})
    POS.update({"Copula": copula})
    POS.update({"Noun Modifier/Noun": noun_modifier})
    if len(modifier) > 0: POS.update({"Adverbs": modifier})
    
    translate_and_print(POS)
    
def process_intransitive(sentence: str) -> dict:
    """A method to process the sentence if a "を" is not in the sentence, denoting that it is intransitive.
    Splits the sentence based on particles and modifiers using methods imported from the Translate module.
    \nEvery part of speech that is not empty if added to the POS dictionary and passed into the 
    translate_and_print() method."""
    subject = []
    verb = []
    verb_ending = ""
    indirect_object = []
    modifier = []
    location = []
    POS = {}
    
    if "に" in sentence:
        subject_phrase = ""
        if "は" not in sentence: 
            if "が" not in sentence: subject_phrase = "私"
            else: subject_phrase = sentence[:sentence.index("が")]
        else: subject_phrase = sentence[:sentence.index("は")]
        
        if len(subject_phrase) >= 3:
            split_modifier = Translate.find_modifiers(subject_phrase)
            if len(split_modifier) >= 2:
                modifier.append(split_modifier[0])
                subject_phrase = split_modifier[1]

        if "の" in subject_phrase:
            split_by_no = Translate.split_no(subject_phrase)
            #Adding the subject phrase at position 0, the word before no at 1, and the word after at 2
            subject.append(subject_phrase)
            subject.append(split_by_no[0])
            subject.append(split_by_no[1])
        else: subject.append(subject_phrase)
        
        verb_phrase_list = Translate.strip_hiragana(sentence[sentence.index("に") + 1:])
        if len(verb_phrase_list[0]) != 0: verb.append(verb_phrase_list[0])
        verb_ending = "" if len(verb_phrase_list[1]) == 0 else verb_phrase_list[1]
        
        sentence_until_ni = Translate.split_by_particle(sentence[:sentence.index("に")])
        location_phrase = sentence_until_ni[-1]
        if len(location_phrase) >= 3:
            split_modifier = Translate.find_modifiers(location_phrase)
            if len(split_modifier) >= 2:
                modifier.append(split_modifier[0])
                location_phrase = split_modifier[1]

        if "の" in location_phrase:
            split_by_no = Translate.split_no(location_phrase)
            #Adding the subject phrase at position 0, the word before no at 1, and the word after at 2
            location.append(location_phrase)
            location.append(split_by_no[0])
            location.append(split_by_no[1])
        else: location.append(location_phrase)
        
    elif "が" in sentence:
        if "は" in sentence: subject_phrase = sentence[:sentence.index("は")]
        else: subject_phrase = sentence[:sentence.index("が")]
            
        if len(subject_phrase) >= 3:
            split_modifier = Translate.find_modifiers(subject_phrase)
            if len(split_modifier) >= 2:
                modifier.append(split_modifier[0])
                subject_phrase = split_modifier[1]

        if "の" in subject_phrase:
            split_by_no = Translate.split_no(subject_phrase)
            #Adding the subject phrase at position 0, the word before no at 1, and the word after at 2
            subject.append(subject_phrase)
            subject.append(split_by_no[0])
            subject.append(split_by_no[1])
        else: subject.append(subject_phrase)
        
        verb_phrase_list = Translate.strip_hiragana(sentence[sentence.index("が") + 1:])
        if len(verb_phrase_list[0]) != 0: verb.append(verb_phrase_list[0])
        verb_ending = "" if len(verb_phrase_list[1]) == 0 else verb_phrase_list[1]
        
        sentence_until_ga = Translate.split_by_particle(sentence[:sentence.index("が")])
        indirect_object_phrase = sentence_until_ga[-1]
        if len(indirect_object_phrase) >= 3:
            split_modifier = Translate.find_modifiers(indirect_object_phrase)
            if len(split_modifier) >= 2:
                modifier.append(split_modifier[0])
                indirect_object_phrase = split_modifier[1]

        if "の" in indirect_object_phrase:
            split_by_no = Translate.split_no(indirect_object_phrase)
            #Adding the subject phrase at position 0, the word before no at 1, and the word after at 2
            indirect_object.append(indirect_object_phrase)
            indirect_object.append(split_by_no[0])
            indirect_object.append(split_by_no[1])
        else: indirect_object.append(indirect_object_phrase)
    elif "は" in sentence:
        subject_phrase = sentence[:sentence.index("は")]
        if len(subject_phrase) >= 3:
            split_modifier = Translate.find_modifiers(subject_phrase)
            if len(split_modifier) >= 2:
                modifier.append(split_modifier[0])
                subject_phrase = split_modifier[1]

        if "の" in subject_phrase:
            split_by_no = Translate.split_no(subject_phrase)
            #Adding the subject phrase at position 0, the word before no at 1, and the word after at 2
            subject.append(subject_phrase)
            subject.append(split_by_no[0])
            subject.append(split_by_no[1])
        else: subject.append(subject_phrase)
        
        verb_phrase_list = Translate.strip_hiragana(sentence[sentence.index("は") + 1:])
        if len(verb_phrase_list[0]) != 0: verb.append(verb_phrase_list[0])
        verb_ending = "" if len(verb_phrase_list[1]) == 0 else verb_phrase_list[1]
        
        
    POS.update({"Subject": subject})
    if len(verb) > 0: POS.update({"Verb": verb})
    if len(indirect_object) > 0: POS.update({"Object": indirect_object})
    if len(verb_ending) > 0: POS.update({"Verb Ending": verb_ending})
    if len(modifier) > 0: POS.update({"Modifier": modifier})
    if len(location) > 0: POS.update({"Location/Object": location})
    
    translate_and_print(POS)
        
def translate_and_print(dic: dict) -> None:
    """A method to translate each value passed into the parameterized dictionary.
    Uses a loop to read the values from the list in the dictionary values, which is printed in a specified format.
    \nAlso includes a line at the end of the output that prints a translation using the Google Translate module."""
    print("\n------------------------------------------------")
    print("Original Sentence: " + sentence_to_be_translated)
    
    for key, value in dic.items():
        description = ["", "", "", ""]
        if key == "Verb Ending":
            english_translation = Translate.translate_verb_ending(value)
            print(key + ": " + value)
            print("\tDefinition in English: " + english_translation[0])
            print("\tFormality: " + english_translation[1])
        elif key == "Copula":
            english_translation = Translate.translate_copula(value)
            print(key + ": " + value)
            print("\tDefinition in English: " + english_translation[0])
            print("\tFormality: " + english_translation[1])
        else:
            for x in value:
                if "の" in x: continue
                description = Translate.translate_from_common(x)#0 is japanese, 1 is english, 2 is hiragana, 3 is part of speech     
                print(key + ": " + x)
                print("\tDefinition in English: " + description[1])
                print("\tReading: " + description[2])
                print("\tPart of Speech: " + description[3])
   
    print("Translation from Google: " + GoogleTranslate.translate_text(text=sentence_to_be_translated,target="en"))
    print("------------------------------------------------\n")
        

def main():
    """The main method which gets the input from the user and processes the 
    it depending on the transitiveness of the verb and copulas.
    \nThe method uses a loop to control when the program is exited."""
    global sentence_to_be_translated
    sentence_to_be_translated = get_input_from_user()
    
    while sentence_to_be_translated != "x":
        if Translate.is_english(sentence_to_be_translated):
            print("\nPlease enter a sentence in Japanese. The program will output the results as the English translation.\n")
            sentence_to_be_translated = get_input_from_user()
            continue
        
        #Decide whether the sentence contains a transitive verb or not
        if "を" in sentence_to_be_translated: process_transitive(sentence_to_be_translated)
        else: 
            if Translate.checkCopula(sentence_to_be_translated): process_copula(sentence_to_be_translated)
            else: process_intransitive(sentence_to_be_translated)
        
        sentence_to_be_translated = get_input_from_user()
    print("Goodbye!")
    

if __name__ == "__main__":
    main()
