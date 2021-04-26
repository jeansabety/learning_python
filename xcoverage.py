#!/usr/bin/env python3

# Write a program that simulates random read coverage over a chromosome
# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line
# Note that you will not sample the ends of a chromosome very well
# So don't count the first and last parts of a chromsome

#I do not understand what this assignment is asking 
#have a genome, fill it up with reads, does some region have 2x as much 
#1 sequencing read that cover x amount of base pairs 
#repeat and then see how many nt were read more than once 
#how much sequencing do you need to do to cover the entire genome
#genome is 100 bp long, read= 10, 1x coverage = 10 reads (enough to go over the genome once) but does this actually happen? 


import sys
import random

gen_size = int(sys.argv[1])
rnum = int(sys.argv[2])
rlen = int(sys.argv[3])

#1. empty set of zeros for the genome 
genome = [0] * gen_size 
#print(genome)

#for every read, pick a random starting point, and then read 
for i in range(rnum) : #do this for the number of reads
	#print(i)
	x = random.randint(0, len(genome) - rlen) #choose a random value in the genome, do not want to sampel anything that "falls off" - last reads last value should be the last value of the list
	for j in range(rlen) : 
		#print(x +j)
		genome[x+j] += 1 #j will be every value as long as the read length, will add one to the next value everytime we run through the loop
	
#print(genome)

#minimum, max, avg: 
min = genome[rlen] #don't want to sample ends because they get sampled less
max=genome[rlen]
total = 0
for n in genome[rlen:-rlen]: #-1 = last values, once again you don't want to sample ends
	if n<min : min = n
	if n>max : max = n
	total += n #n will be the number of times the nt was counted
print(min, max, total/(gen_size - 2*rlen)) 



"""
python3 xcoverage.py 1000 100 100
5 20 10.82375
"""
