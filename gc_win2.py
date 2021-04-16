#!/usr/bin/env python3

# Write a program that computes the GC fraction of a DNA sequence in a window
# Window size is 11 nt
# Output with 4 significant figures using whichever method you prefer
# Use no nested loops. Instead, count only the first window
# Then 'move' the window by adding 1 letter on one side
# And subtracting 1 letter from the other side
# Describe the pros/cons of this algorith vs. nested loops

seq = 'ACGACGCAGGAGGAGAGTTTCAGAGATCACGAATACATCCATATTACCCAGAGAGAG'
#seq = '0123456789'
w = 11

A = 0 
C = 0 
T = 0 
G = 0 
#1. count the numbers of actg within the first window
for i in range(w) : #only want to count first window 
	if seq[i] == 'A' : A += 1
	elif seq[i]== 'T' : T += 1
	elif seq[i] == 'C' : C +=1 
	else : G += 1

#now actg = the number of them within the first window
#now want to move the window 

for i in range(len(seq) -w) : #want to stop at -w so all windows have 11 characters
	off = seq[i] #seq[i]= nt coming off when window moves 
	on = seq[i+w] #seq[i+w] = nt being added when window moves 
	if off == 'A'   : A -= 1 #if A is being removed, -1 from total amount of As
	elif off == 'T' : T -= 1
	elif off == 'G' : G -= 1
	elif off == 'C' : C -= 1 #dont need to end with else
	
	if on == 'A'   : A += 1 #need two ifs because having only means that we are only taking it off, because - occurs first 
	elif on == 'T' : T += 1
	elif on == 'C' : C += 1
	else           : G += 1 
	print(i, seq[i:i+w], f'{(G+C)/w:.4f}')

#this is a faster way to do it 
#other way is more simple 

"""	
python3 gc_win2.py
0 ACGACGCAGGA 0.6364
1 CGACGCAGGAG 0.7273
2 GACGCAGGAGG 0.7273
3 ACGCAGGAGGA 0.6364
4 CGCAGGAGGAG 0.7273
5 GCAGGAGGAGA 0.6364
6 CAGGAGGAGAG 0.6364
7 AGGAGGAGAGT 0.5455
8 GGAGGAGAGTT 0.5455
9 GAGGAGAGTTT 0.4545
10 AGGAGAGTTTC 0.4545
11 GGAGAGTTTCA 0.4545
12 GAGAGTTTCAG 0.4545
13 AGAGTTTCAGA 0.3636
14 GAGTTTCAGAG 0.4545
15 AGTTTCAGAGA 0.3636
16 GTTTCAGAGAT 0.3636
17 TTTCAGAGATC 0.3636
18 TTCAGAGATCA 0.3636
19 TCAGAGATCAC 0.4545
20 CAGAGATCACG 0.5455
21 AGAGATCACGA 0.4545
22 GAGATCACGAA 0.4545
23 AGATCACGAAT 0.3636
24 GATCACGAATA 0.3636
25 ATCACGAATAC 0.3636
26 TCACGAATACA 0.3636
27 CACGAATACAT 0.3636
28 ACGAATACATC 0.3636
29 CGAATACATCC 0.4545
30 GAATACATCCA 0.3636
31 AATACATCCAT 0.2727
32 ATACATCCATA 0.2727
33 TACATCCATAT 0.2727
34 ACATCCATATT 0.2727
35 CATCCATATTA 0.2727
36 ATCCATATTAC 0.2727
37 TCCATATTACC 0.3636
38 CCATATTACCC 0.4545
39 CATATTACCCA 0.3636
40 ATATTACCCAG 0.3636
41 TATTACCCAGA 0.3636
42 ATTACCCAGAG 0.4545
43 TTACCCAGAGA 0.4545
44 TACCCAGAGAG 0.5455
45 ACCCAGAGAGA 0.5455
46 CCCAGAGAGAG 0.6364
"""
