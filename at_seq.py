#!/usr/bin/env python3

import random
random.seed(1) # comment-out this line to change sequence each time, seeding it will make it choose the same number every time it runs, good for debugging 
# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence


#profs solution: 
bp = 30 #how many nt we want 
seq = ''
at = 0
for i in range(bp):
	r = random.random() #generate a random number, random number generator only goes from 0-1 (non inclusive)
	if   r < 0.30: #if random number is less than .3, make it a A 
		seq += 'A'
		at += 1
	elif r < 0.50: 
		seq += 'C'
	elif r < 0.70:
		seq += 'G'
	else:
		seq += 'T'
		at += 1

print(bp, at/bp, seq)


#class solution 1:
bp2 = 30
seq2 = ''
T = 0.6 #this is our threshold 
for i in range(bp2):
	p = random.random() #p for probability 
	if p < T : seq2 += random.choice('AT') #randomly choose A or T 
	else     : seq2 += random.choice('GC')
print(bp2, at/bp2, seq2)

#class solution 2: 
bp3 = 30
seq3 = ''
T = 0.6 #this is our threshold 
for i in range(bp3) :
	p = random.random() 
	if p < T :
		if random.random() < 0.5 : seq3 += 'A' #random choose a number, if it is less than .5, make it an A 
		else                     : seq3 += 'T'
	else : 
		if random.random() < 0.5 : seq3 += 'G'
		else                     : seq3 += 'C'	
print(bp3, at/bp3, seq3)

#class solution 3: 
bp4 = 30
seq4 =''
for i in range(bp4) : 
	r = random.choice('AAATTTCCGG') #correct proportion of AT to CG
	seq4 += r #add that number to seq4 (every i so 30 times)
print(bp4, at/bp4, seq4)
	






"""
python3 at_seq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
