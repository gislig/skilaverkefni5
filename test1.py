import random
import string

def get_word_string(filename):
    try:
        file_object  = open(filename)
        return file_object.read()
    except Exception:
        print("file not exist")

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
    

def scramble_string(word_string):
    new_word_list = []
    sentence = ""
    for word in word_string.split():

        new_word = scramble_word(word)
        print(new_word)


random.seed(10)
filename = "bla.txt"
word_string = get_word_string(filename)
scramble_string(word_string)
#scramble_string("doesn't")
#should be dose'nt


