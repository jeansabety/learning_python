#!/usr/bin/env python3

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

dna = 'ACTGAAAAAAAAAAA'

#version 1: 

rcdna1 = ''
for i in range(len(dna) -1, -1, -1) : 
	nt = dna[i] 
	if   nt == 'A' : nt = 'T'
	elif nt == 'T' : nt = 'A'
	elif nt == 'C' : nt = 'G' 
	elif nt == 'G' : nt = 'C'
	else           : nt = 'N' 
	rcdna1 += nt
print(rcdna1)

#version 2: 

rcdna2 = ''
for i in reversed(range(len(dna))): 
	nt = dna[i]
	if nt == 'A'  : c = 'T' 
	elif nt == 'T': c = 'A'
	elif nt == 'C': c = 'G'
	else          : c = 'C'
	rcdna2 += c 
print(rcdna2)

#version 3: 

rcdna3 = ''
for nt in dna[::-1]: #from 0 to end of string, go by -1
	if nt == 'A'   : rcdna3 += 'T' 
	elif nt == 'T' : rcdna3 += 'A'
	elif nt =='C'  : rcdna3 += 'G'
	elif nt == 'G' : rcdna3 += 'C'
	else           : nt = 'N'
print(rcdna3)
	
#version 4: 

rcdna4 = ''
for i in range(len(dna) -1, -1, -1): 
	nt = dna[i]
	if nt == 'A'   : rcdna4 += 'T'
	elif nt == 'T' : rcdna4 += 'A'
	elif nt == 'G' : rcdna4 += 'C'
	elif nt == 'C' : rcdna4 += 'G'
	else           : rcdna4 += 'N'
print(rcdna4)

#done

"""
python3 anti.py
TTTTTTTTTTTCAGT
"""
