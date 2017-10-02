nuc = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
def to_rna(sequence):
    return "".join([nuc[i] for i in sequence])
