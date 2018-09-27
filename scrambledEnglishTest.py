import random
import string

def find_punctiations(word_string):
    punks = []
    for index, word in enumerate(word_string.split(" ")):
        for letter in word:
            contains_punk = False
            if letter in string.punctuation:
                contains_punk = True

        new_punk = []
        if contains_punk == True:
            new_punk = [index,word]
            punks.append(new_punk)
            
    return punks

def remove_punctiations(word):
    new_word = ""
    for n in word.strip():
        if n not in string.punctuation:
            new_word += n

    return new_word

def scramble_word(index,word):
    new_word = ""
    old_word = remove_punctiations(word)
    word_count = len(old_word)
    if word_count > 1:
        first_letter = new_word[0]
        last_letter = new_word[word_count-1]
        word_to_scramble = list(new_word[1:word_count-1])

def scramble_test(word_string):
    new_sentence = []
    for index, word in enumerate(word_string.split(" ")):

        word_count = len(word)
        if word_count > 1:
            first_letter = word[0]
            last_letter = word[word_count-1]

            word_to_scramble = list(word[1:word_count-1])
            random.shuffle(word_to_scramble)
            new_scrambled_word = str(scrambled_str.join(word_to_scramble))

            scrambled_str = "{}{}{}".format(first_letter,new_scrambled_word,last_letter)
            new_sentence.append(scrambled_str)
        else:
            new_sentence.append(word)
    
    theoutput = ' '.join(new_sentence)
    punk_list = find_punctiations(word_string)
    print(punk_list)
    for punk in punk_list:
        index, punk_to_add = punk

    return theoutput

def scramble_string(word_string):
    new_sentence = []
    for word in word_string.split(" "):
        scrambled_str = ""
        word_count = len(word)
        if word_count > 1:
            first_letter = word[0]
            last_letter = word[word_count-1]

            word_list = list(word[1:word_count-1])
            random.shuffle(word_list)
            thelist = str(scrambled_str.join(word_list))
            scrambled_str = "{}{}{}".format(first_letter,thelist,last_letter)
            
            new_sentence.append(scrambled_str)
        else:
            new_sentence.append(word)

    return new_sentence

random.seed(10)

word_string = "According to research at an English university, it does'nt matter in what order the letters in a word are, the only important thing is that the first and last letter is a the right place. The rest can be a total mess and you can still read it without any problem. This is because we do not read every letter by itself but the word as a whole."
correct_output = "Acionrcdg to reecrash at an Elsginh uiirtnvsey, it dose'nt mttaer in what oedrr the lertets in a wrod are, the olny imtroanpt tnihg is that the fisrt and lsat lteetr is a the rhgit pacle. The rset can be a toatl mses and you can sitll raed it wtiuhot any pbloerm. Tihs is bescuae we do not raed every leettr by ilestf but the word as a wolhe."

print(scramble_test(word_string))

print(remove_punctiations(".word."))
#print(find_punctiations(word_string))

#output = ' '.join(scramble_string(word_string))
#
#for c_word in correct_output.split(" "):
#    if c_word not in output:
#        print(c_word)

#print(output)

#output = ' '.join(scramble_string(word_string))
#if output == correct_output:
#    print("Correct!!!")
#else:
#    print("Incorrect!! :(")
#print(scramble_string(word_string))
#print(correct_output)