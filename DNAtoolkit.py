# DNA Toolkit file
import collections

Nucleotides = ["A", "C", "G", "T"]

#Check desired sequence to verify if it is a valid DNA string

def validateSeq(DNA_sequence):
        tmpseq = DNA_sequence.upper()
        for nt in tmpseq:
            if nt not in Nucleotides:
                return False
        return tmpseq

def CountNucleotide(seq):
    return dict(collections.Counter(seq))
    