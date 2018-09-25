import random

def scramble_string(word_string):
    for word in word_string.split(" "):
        scrambled_str = ""
        
        word_count = len(word)
        if word_count > 1:
            first_letter = word[0]
            last_letter = word[word_count-1]

            word_list = list(word[1:word_count-1])
            random.shuffle(word_list)
            scrambled_str = first_letter + scrambled_str.join(word_list) + last_letter
            print(scrambled_str)
        else:
            print(word)
        
random.seed(10)
word_string = "Four score and seven years ago our fathers brought forth on this continent a new nation"

print(scramble_string(word_string))