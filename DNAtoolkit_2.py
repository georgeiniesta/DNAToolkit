# DNA Toolkit file

Nucleotides = ["A", "C", "G", "T"]

#Check desired sequence to verify if it is a valid DNA string

def validateSeq(DNA_sequence):
        tmpseq = DNA_sequence.upper()
        for nt in tmpseq:
            if nt not in Nucleotides:
                return False
        return tmpseq

# Count nt in desired function

def countNucleotideFrequency(sequence)
    tmpFrequencyDict = {"A":0, "C":0,"G":0,"T":0,}
        for nt in sequence:
            tmpFrequencyDict[nt] += 1
        return tmpFrequencyDict