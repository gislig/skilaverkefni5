import string
import random

# Opna skjalið og setja það í streng
def get_word_string(filename):
    try:
        file_contents = open(filename)
        file_contents = file_contents.read()
        # Hreinsar út alla enter/return takka
        file_contents = file_contents.replace("\n"," ")
        return file_contents
    except:
        print("File {} not found".format(filename))

# Finna punkta og kommur og setja indexinn ásamt hvað
# á að koma eftir breytingu á orði
def find_punk(word):
    punks = []
    for index, letter in enumerate(word):
        contains_punk = False
        # Ef orðið inniheldur punctations þá setur hún contains_punk í True
        if letter in string.punctuation:
            contains_punk = True

        # Orðið með punctations þá setur hún það í lista, hvar orðið er, hvað orðið er og stafurinn
        if contains_punk == True:
            punks = [index, word, letter]
    return punks

# Setur inn punkta, komur eða annað þar sem á við
def add_punk(index,punk,word):
    # Síður samnan orðið með staðsetningu á punc og skilar því til baka
    new_word = str(word[:index] + punk + word[index:])
    return new_word

# Skramblar orðið
def scramble_word(word):
    # Sækir lengd orðs til að finna út enda á orði
    word_count = len(word)
    new_word = ""
    if word_count > 1:
        # Setja fyrsta og síðasta stafinn í streng og er notaður síðar
        first_letter = word[0]
        last_letter = word[word_count-1]
        # Tekur stafi á milli orðs og setur það í lista
        new_word = list(word[1:word_count-1])
        # Scrambla orð
        random.shuffle(new_word)
        # Þegar er búið að scrambla orð setja það samann aftur
        new_scrambled_word = str(''.join(new_word))
        new_word = "{}{}{}".format(first_letter,new_scrambled_word,last_letter)
    return new_word

# Les orðið og finnur út hvernig á að vinna með það
def read_word(word):
    # Sækir staðsetningar á punctuations
    punk_word = find_punk(word)
    scrambled_word = ""
    
    # Athugar hvort að orðið sé punctiation orð ef svo er þá fer hún í hreinsun. Annars fer hún í að scrambla orð
    if punk_word != []:
        # Þetta virðist vera eina leiðin til að fixa, vandamál virðist vera með uppi kommu að rest komi rétt
        word_to_scramble = word.replace(".","").replace(",","").replace("'","x")
        scrambled_word = scramble_word(word_to_scramble)
        # Setja inn punctations þar sem á við út frá hvar það var geymt
        scrambled_word = add_punk(punk_word[0],punk_word[2],scrambled_word)
        scrambled_word = scrambled_word.replace("x","")
    elif len(word) == 1:
        # Ekki scrambla orð ef orðið er 1
        scrambled_word = word
    else:
        # Scrambla orð ef það eru engin punctations
        word_to_scramble = word
        scrambled_word = scramble_word(word_to_scramble)
    
    return scrambled_word

# Sækir upplýsingar úr skrá og fer í read_word til að skrambla orð
def scramble_string(word_string):
    new_sentence = ""
    # Athugar hvort að það hafi eitthvað skilað sér í skránni
    if word_string:
        # Fer yfir hvert orð og umbreytir því með read_word
        for index, word in enumerate(word_string.split(" ")):
            if index == 0:
                new_sentence += read_word(word)
            else:    
                new_sentence += " " + read_word(word)

    return new_sentence

# Main program starts here - DO NOT change it
random.seed(10)
filename = input("Enter name of file: ")
word_string = get_word_string(filename)
scrambled_string = scramble_string(word_string)
print(scrambled_string)