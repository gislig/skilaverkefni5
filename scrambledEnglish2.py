import string
import random

# Opna skjalið og setja það í streng
def get_word_string(filename):
    try:
        file_object  = open(filename, encoding="utf-8")
        return file_object.read()
    except Exception:
        print("File {} not found".format(filename))

# Finna punkta og kommur og setja indexinn ásamt hvað
# á að koma eftir breytingu á orði
def find_punk(word):
    punks = []
    for index, letter in enumerate(word):
        contains_punk = False
        if letter in string.punctuation:
            contains_punk = True

        if contains_punk == True:
            punks = [index, word, letter]
    return punks

# Setur inn punkta, komur eða nanað þar sem á við
def add_punk(index,punk,word):
    new_word = str(word[:index] + punk + word[index:])
    return new_word

# Skramblar orðið
def scramble_word(word):
    word_count = len(word)
    new_word = ""
    if word_count > 1:
        first_letter = word[0]
        last_letter = word[word_count-1]
        new_word = list(word[1:word_count-1])
        random.shuffle(new_word)
        new_scrambled_word = str(''.join(new_word))
        new_word = "{}{}{}".format(first_letter,new_scrambled_word,last_letter)
    return new_word

# Les orðið og finnur út hvernig á að vinna með það
def read_word(word):
    punk_word = find_punk(word)
    scrambled_word = ""
    
    if punk_word != []:
        word_to_scramble = word.replace(".","").replace(",","").replace("'","x")
        scrambled_word = scramble_word(word_to_scramble)
        scrambled_word = add_punk(punk_word[0],punk_word[2],scrambled_word)
        scrambled_word = scrambled_word.replace("x","")
    elif len(word) == 1:
        scrambled_word = word
    else:
        word_to_scramble = word
        scrambled_word = scramble_word(word_to_scramble)
    
    return scrambled_word

# Sækir upplýsingar úr skrá og fer í read_word til að skrambla orð
def scramble_string(word_string):
    words = word_string.split(" ")
    new_sentence = ""
    for index, word in enumerate(words):
        if index == 0:
            new_sentence += read_word(word)
        else:    
            new_sentence += " " + read_word(word)

    return new_sentence

# Main program starts here - DO NOT change it
random.seed(10)
#filename = input("Enter name of file: ")
filename = 
word_string = get_word_string(filename)
scrambled_string = scramble_string(word_string)
print(scrambled_string)