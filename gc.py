#!/usr/bin/env python3

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places
# Use all three formatting methods (IN 03 text)

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT' # feel free to change

#want a variable that will hold the number of GCs (gc)
gc = 0 #no idea what it is, do some counting and then figure out what it is 
for i in range(len(dna)):
	if dna[i] == "C" or dna[i] == "G":  #""= letter #if dna letter i is =to c or g
		gc += 1 # add it to gc count 	
#f string formating:	
print(f'{gc/len(dna):.2f}') #take the count and divide by the length of the dna to find percent, .2f -> format to two decimal points

#printf 
print('%.2f' % (gc/len(dna)))

#str
print('{:.2f}'.format(gc/len(dna)))

#done
"""
python3 gc.py
0.42
0.42
0.42
"""
