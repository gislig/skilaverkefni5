import string
import random

# Opna skjalið og setja það í streng
def get_word_string(filename):
    try:
        file_object  = open(filename)
        return file_object.readline()
    except Exception:
        print("File {} not found".format(filename))

def scramble_string(word_string):
    print(word_string)

# Main program starts here - DO NOT change it
random.seed(10)
#filename = input("Enter name of file: ")
filename = "file1.txt"
word_string = get_word_string(filename)
scrambled_string = scramble_string(word_string)
print(scrambled_string)