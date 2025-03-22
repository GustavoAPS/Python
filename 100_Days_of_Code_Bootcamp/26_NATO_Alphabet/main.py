import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet_dict = {}
for (index, row) in data.iterrows():
    alphabet_dict[row.letter] = row.code

def nato():
    name = (input("What is the word to receive in NATO?")).upper()

    try:
        for letters in name:
            print(alphabet_dict[letters])
    except KeyError:
        print("Input must contain only a-z letters")
        nato()

nato()
