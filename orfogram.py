#!/usr/bin/env python3

import argparse
import mcb185 

# In prokaryotic genomes, genes are often predicted based on length
# Long ORFs are not expected to occur by chance
# Write a program that creates a histogram of ORF lengths in random DNA - how many tmes did you see each length 
# Your library should contain new functions for the following
#    1. generating random sequence
#    2. generating ORFs from sequence
# Your program should have command line options for the following:
#    + amount of sequence to generate
#    + GC fraction of sequence
# Thought questions
#    a. how does GC fraction affect the histogram? - stop codons are AT rich 
#    b. what is a good length threshold for a gene?

#create inputs from the command line 
parser = argparse.ArgumentParser(description='explore ORF length')
#if someone doesnt put in a seq length we will use a default one
parser.add_argument('--size', required=False, type=int, default=4500000, #default is the size of the e coli genome 
	metavar='<str>', help='genome size [%(default)i]') #i = int
parser.add_argument('--orfmin', required=False, type=int, default=100, #has a default value that you can overide 
	metavar='<int>', help='minimum orf length [%(default)i]')
parser.add_argument('--gc', required=False, type=float, default=0.5, 
	metavar='<float>', help='gc content [%(default).3f]')
parser.add_argument('--info', action='store_true',
	help='provide additional info')
parser.add_argument('--seed', action='store_true',
	help='fix random seed')
arg = parser.parse_args()
if arg.info: print(arg.size, arg.orfmin, arg.min) #will tell parameters used if the person asks for more info 
if arg.seed: random.seed(1) #the random number needs a seed where it starts, start at the same place every time you run program - the seq will be the same every time - help w debugging

#generate random genome of specified size and gc content 
seq = mcb185.randseq(arg.size, arg.gc)
#print(seq)

#find ORF 
orfs = mcb185.orf(seq) #returns orf legths

histogram = [0] * (max(orfs) + 1) #create an empty list the legth of the longest orf
for n in orfs: 
	histogram[n] += 1 #add one to the value every time you see it (ie add one to the second slot verytime you see 2)
	
#print(histogram)

for i in range(len(histogram)): 
	print("length of orf:", i, "frequency:", histogram[i]) #print i (that length of the orf) and how many tiems it appears

large = 0
for n in histogram[arg.orfmin:]:
	large += n 
print(large) #print the number of orfs that are larger than cutoff 



