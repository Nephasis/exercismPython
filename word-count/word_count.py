import re

def words_split(sentence):
    words = re.sub("[^a-zA-Z0-9]", " ", sentence.lower()).split()
    return words

def word_count(sentence):
    words_dict = {}
    words = re.sub("[^a-zA-Z0-9]", " ", sentence.lower()).split()
    print words
    for i in words:
        z = 1
        print i
        if words[z] == i:
            z += 1
        else:
            pass
        words_dict[i] = z
    print words_dict
