import re

def hey(what):
    sentence = what.strip()
    if sentence.isupper():
        return 'Whoa, chill out!'
    if sentence.endswith('?'):
        return 'Sure.'
    if re.search('[\w]+', sentence) is None:
        return 'Fine. Be that way!'
    else:
        return 'Whatever.'
