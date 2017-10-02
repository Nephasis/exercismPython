import re
from collections import Counter

def word_count(sentence):
    words = re.sub(r"[\W_]+", " ", sentence.decode('utf-8').lower(), flags=re.U).split()
    return Counter(words)
