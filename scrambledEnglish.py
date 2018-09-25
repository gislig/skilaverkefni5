#https://github.com/nyghtowl/Interview_Problems/blob/master/python/scramble.py 

import random
import string

def get_word_string(filename):
    return 0

def scramble_string(word_string):
    for word in word_string.split(" "):
                    

# Main program starts here - DO NOT change it
random.seed(10)
#filename = input("Enter name of file: ")
#word_string = get_word_string(filename)

word_string = "Four score and seven years ago our fathers brought forth on this continent a new nation"

scrambled_string = scramble_string(word_string)
print(scrambled_string)