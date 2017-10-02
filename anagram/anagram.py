import collections

compare = lambda x, y: collections.Counter(x) == collections.Counter(y)

def detect_anagrams(main_word, word_list):
    anagrams = []
    for word in word_list:
        if word.lower() != main_word.lower() and compare(main_word.lower(), word.lower()):
            anagrams.append(word)
    return anagrams
