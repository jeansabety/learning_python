#!/usr/bin/env python3

# Write a program that prints out the position, frame, and letter of the DNA
# Try coding this with a single loop
# Try coding this with nested loops

dna = 'ATGGCCTTT'

for i in range(len(dna)) : 
	print(i, i%3 , dna[i]) #i%3 -> divide i (which is a number!) by i, and print the remainder 

for i in range(0, len(dna), 3) : #i = 0, 3, 6, 9
	for j in range(3) : # j = 0,1,2 
		print(i+j, j, dna[i+j]) #i+j -> number of characters in dna (0+0, 0+1, 0+2, 3+0...) // j -> "frame" // dna[i+j] -> dna[1..9]



"""
python3 frame.py
0 0 A
1 1 T
2 2 G
3 0 G
4 1 C
5 2 C
6 0 T
7 1 T
8 2 T
"""
