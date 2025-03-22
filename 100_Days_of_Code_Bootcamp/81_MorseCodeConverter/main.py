conversions = {
    'a': '* -',
    'b': '- * * *',
    'c': '- * - *',
    'd': '- * *',
    'e': '*',
    'f': '* * - *',
    'g': '- - *',
    'h': '* * * *',
    'i': '* *',
    'j': '- * * *',
    'k': '- * -',
    'l': '* - * *',
    'm': '- -',
    'n': '- *',
    'o': '- - -',
    'p': '* - - *',
    'q': '- - * -',
    'r': '* - *',
    's': '* * *',
    't': '-',
    'u': '* * -',
    'v': '* * * -',
    'w': '* - -',
    'x': '- * * -',
    'y': '- * - -',
    'z': '- - * *'
}

input_string = (input("What do you want to convert to morse code?\n")).lower()

for n in input_string:
    if n in conversions:
        print(conversions[n])
