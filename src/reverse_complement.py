def rev_complement_dna(sequence) :
    sequence = sequence.upper()
    complement = {'A':'T', 'G':'C', 'T':'A', 'C':'G'}
    reverse_comp = "".join(complement[base] for base in reversed(sequence))
    return reverse_comp



def rev_complement_rna(sequence) :
    sequence = sequence.upper()
    complement = {'A':'U', 'G':'C', 'U':'A', 'C':'G'}
    reverse_comp = "".join(complement[base] for base in reversed(sequence))
    return reverse_comp



