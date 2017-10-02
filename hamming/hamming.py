import operator

def distance(seq1, seq2):
    if len(seq1) == len(seq2):
        return sum(map(operator.ne, seq1, seq2))
