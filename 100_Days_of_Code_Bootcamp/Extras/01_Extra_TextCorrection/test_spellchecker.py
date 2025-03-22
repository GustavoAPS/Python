from spellchecker import SpellChecker
spell = SpellChecker(language='pt')


def correct(input_text):
    return spell.correction(input_text)

# Pacote
# pip install pyspellchecker
