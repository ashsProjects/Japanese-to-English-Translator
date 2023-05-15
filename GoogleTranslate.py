from googletrans import Translator

def translate_text(text, target="en") -> str:
    """A method that uses the googletrans module to translate a given text to a target language.
    \nThe method will be utilized exclusively in the program to translate Japanese into English."""
    translator = Translator()
    translated_text = translator.translate(text, dest=target)
    return translated_text.text

    