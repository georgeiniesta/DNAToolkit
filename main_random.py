# DNA Toolset/Code Testing file

from DNAtoolkit import *
import random

#Create a random DNA sequence

randomDNAstring = ''.join ([random.choice(Nucleotides)
                            for nt in range(20)])

print (validateSeq(randomDNAstring))
print (CountNucleotide(randomDNAstring))