#!/usr/bin/env python3

# Print out all the codons for the sequence below in reading frame 1
# Use a 'for' loop

dna = 'ATAGCGAATATCTCTCATGAGAGGGAA'

for i in range(0, len(dna), 3): # i = every third character between A and A (1st and last dna characters)
	print(dna[i:i+3]) #print i through i+3 (every third character + the two following characters)

#originally did print(dna(i)) but that only gave one nucleotide at a time so I had to to codon 1 to codon 1+3 so I could get sets of 3 
#this notation does not make any sense to me 

	
"""
python3 codons.py
ATA
GCG
AAT
ATC
TCT
CAT
GAG
AGG
GAA
"""