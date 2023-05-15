import csv
import BasicWords
import string

def split_by_particle(sentence: str) -> list:
    """A method to split the sentence passed in as a parameter with particles 
    and returns a list. The list of particles are imported from the BasicWords
    module in the same library."""
    particles = BasicWords.particles_list()
    temp_untranslated = ""
    split_list = []
    
    for x in sentence:
        if x in particles:
            split_list.append(temp_untranslated)
            split_list.append(x)
            temp_untranslated = ""
        else:
            temp_untranslated += x
    
    split_list.append(temp_untranslated)
    return split_list
      
def find_coupla(sentence: str) -> list:
    """A method to find the copula within the string. Also checks for
    ending particles such as "" and "". \nReturns a list with the copula
    as the 2nd element and rest of the sentence as the 1st."""
    ending_particle = ["ね", "よ"]
    copula = BasicWords.copulas().keys()
    
    temp_untranslated = ""
    split_list = []
    
    for x in reversed(sentence):
        if temp_untranslated in copula:
            split_list.append(temp_untranslated)
            split_list.append(sentence[:sentence.index(temp_untranslated)])
            break
        elif x in ending_particle:
            split_list.append(x)
            temp_untranslated = ""
        else:
            temp_untranslated  = x + temp_untranslated
            
    if len(split_list) == 0: split_list.append(temp_untranslated)
    return list(reversed(split_list))

def checkCopula(sentence: str) -> bool:
    """A method to check if the sentence contains a copula. Uses the find_copula() method to check.
    \nReturns a bool."""
    list_to_check = find_coupla(sentence)
    return len(list_to_check) > 1

def translate_from_common(words: str) -> list[str]:
    """A method to check if a word is contaied in the common_japanese.csv file.
    \nChecks if the word is contained in the 
    first index of the line and returns that line if true."""
    with open ("common_japanese.csv", "r", encoding="UTF8") as common_words:
        csv_reader = csv.reader(common_words)

        for line in csv_reader:
            if words in line[0]:
                matched_word = line[0]
                if matched_word == words: return line
                elif words in matched_word: 
                    if len(matched_word) == 2 and matched_word[1] in BasicWords.hiragana(): return line
                    elif len(matched_word) == 3 and matched_word[2] in BasicWords.hiragana(): return line
        return ["", "", "", ""]
    
def strip_hiragana(text: str) -> list:
    """A method to seperate the hiragana characters from the kanji. Used for checking the verb ending.
    \nReturns a list with kanji characters in the 1st index and the hiragana characters in the 2nd index
    if there hiragana was present. Else, returns a list with the original text in the 1st index."""
    hiragana_list = BasicWords.hiragana()
    no_hiragana = ""
    hiragana = ""
    return_list = []
    
    for t in text:
        if t == "。": break
        elif t in hiragana_list: hiragana += t
        else: no_hiragana += t
        
    return_list.append(no_hiragana)
    return_list.append(hiragana)
    
    return return_list

def translate_verb_ending(ending: str) -> list:
    """A method to translate the ending of the verb depending on the tenses.
    \nChecks for irregular verbs such as suru, aru, iru, and iku as well as 
    regular forms along with their te forms."""
    suru = BasicWords.suru_conjugations()
    other = BasicWords.verb_conjugations()
    te = BasicWords.te_conjugations()
    aru = BasicWords.aru_conjugations()
    iru = BasicWords.iru_conjugations()
    iku = BasicWords.iku_conjugations()
    
    if ending in suru: return suru.get(ending)
    else:
        if "て" in ending:
            te_ending = ending[ending.index("て") + 1:]
            te_ending = te_ending.replace("い", "", 1)
            return te.get(te_ending)
        elif "で" in ending:
            te_ending = ending[ending.index("で") + 1:]
            te_ending = te_ending.replace("い", "", 1)
            return te.get(te_ending)
        elif ending.startswith("あ"):
            return aru.get(ending)
        elif ending.startswith("い"):
            return iru.get(ending)
        elif "行" in ending:
            return iku.get(ending)
        else:
            for key, value in other.items():
                if key in ending: return value
            return ["doing", "casual"]
                
def translate_copula(word: str) -> list:
    """A method to translate the copula using a list of copulas imported from BasicWords module."""
    copulas_list = BasicWords.copulas()
    
    for key, value in copulas_list.items():
        if word == key: return value

def is_english(text: str):
    """A method to check if the text from parameter is written in English.
    \nReturns a bool."""
    return all(char in string.ascii_letters or char in string.punctuation or char.isspace() for char in text)

def find_modifiers(sentence) -> list:
    """A method to find the modifier within a sentence using a list of modifiers and adverbs imported from the BasicWords module.
    \nReturns a list with the modifier in the 1st index and the rest of the sentence in the 2nd."""
    modifiers = BasicWords.adverbial_nouns()
    return_list = []
    
    for adverb in modifiers.keys():
        if adverb in sentence:
            return_list.append(adverb)
            return_list.append(sentence[sentence.find(adverb) + len(adverb):])
    return_list.append(sentence)
        
    return return_list
    
def split_no(sentence: str) -> list:
    """A method to split the given sentence by the particle の.
    \nReturns a list with the word before の in the 1st index and word after の in the 2nd."""
    return_list = []
    no_index = sentence.index("の")
    
    #0 is first word, 1 is の, 2 is second word
    return_list.append(sentence[:no_index])
    return_list.append(sentence[no_index + 1:])
    
    return return_list