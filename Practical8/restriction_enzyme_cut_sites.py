def restriction_enzyme_cut_sites(DNA_sequence,sequence_recognised):
    canonical_nucleotides=['A','C','G','T']
    length_of_DNA_sequence=len(DNA_sequence)
    length_of_sequence_recognised=len(sequence_recognised)
    for i in DNA_sequence:
        if i in canonical_nucleotides:
            continue
        else:
            print('DNA sequence must only contain canonical (‘ACGT’) nucleotides')
            return None
    for i in sequence_recognised:
        if i in canonical_nucleotides:
            continue
        else:
            print('Sequence recognised must only contain canonical (‘ACGT’) nucleotides')
            return None
    cut_sites=[]
    for i in range(length_of_DNA_sequence-length_of_sequence_recognised+1):
        if DNA_sequence[i:i+length_of_sequence_recognised]==sequence_recognised:
            cut_sites.append(i)
    return cut_sites
DNA_sequence='GTAGATGCAAGTGGTGGTAGTGTCTGTTCTGAGAGGGTAGCCTAA'
sequence_recognised='GTAG'
cut_sites=restriction_enzyme_cut_sites(DNA_sequence,sequence_recognised)
print(f'Positions within the DNA sequence where the restriction enzyme cuts are {cut_sites}')
