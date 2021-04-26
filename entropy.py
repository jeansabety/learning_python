#!/usr/bin/env python3

# Write a Shannon entropy calculator: H = -sum(pi * log(pi)) - every value of histogram and add probability of value * long of prob
	#how hard it is to predict the thing 
	#more skewed the values -> should get a value of less than 1 which means it is more predictable 
# The values should come from the command line
# E.g. python3 entropy.py 0.4 0.3 0.2 0.1
# Put the probabilities into a new list
# Don't forget to convert them to numbers
#later will use an entropy filter to filter out low entropy areas of dna 


import math
import sys

#-----make command line props numbers and add to a list------#
p = [] #want to make a list so you can convert all at once and not include the file name
for s in sys.argv[1:] : #for every number on command line... start at 1 bc 0 is file name
	p.append(float(s)) #make values on command line floating point numbers and add to list p 

#--------check to make sure the p values are = to 1-------#
#print(sum(p)) - can look to see if it is near 1 with your eyes
#if sum(p) != 1 - if sum is not = to 1 -> can't do because we are using floating point num 
assert(math.isclose(sum(p), 1, abs_tol=0.2)) #if p is not close to 1 (within 0.2 - this is optional, math has default limit)-> program should fail 


#-----do the math------#
H = 0 
for i in range(len(p)) : 
	H -= p[i] * math.log2(p[i])
print(H)

"""
or: 
p = []  - empty container to put all values in 
for i in range(1, len(sys.argv)) : - length of sys.argv 
	p.append(float(sys.argv[i])  - add what is on command structure to list as flaotin point number 

python3 entropy.py 0.1 0.2 0.3 0.4
1.846
"""
