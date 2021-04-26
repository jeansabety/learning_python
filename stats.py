#!/usr/bin/env python3

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import the stats library!

import sys
import math

#1. make all values on the command line intergers and add them to a list
stat_values = []
for i in sys.argv[1:] :
	stat_values.append(int(i))
		
#print(stat_values)

#2. count 
#for every item in the list, add one, print out at the end: 
count = 0 #place outside of 
for i in stat_values : 
	count += 1 
print("Count:", count)

# or - print("Count:", len(stat_values))

#3. minimum : 
#sort, print out first element
#stat_values.sort()
#print("Minimum:", stat_values[0])

min = stat_values[0]
for i in stat_vales[1:]: 
	if i < min : min = i

#4. maximum : sort, print out last element - how do i do that
print("Maximum:", stat_values[len(stat_values)-1]) 

#5. Mean : 
#every time we go through loop, add value to empty set, 
sumsv = 0
for i in stat_values: 
	sumsv += i #why doesn't this work with stat_values[i]? 
#the divide empty set by number of values
mean = sumsv/len(stat_values) 
print("Mean:", f'{mean:.3f}')


#6. standard deviation: 
# a. (x - mean)^2 for all values
x = 0 
for i in stat_values: 
	num = (i - mean)**2
#b. add that 
	x += num
#print(x)
#c. divide by num of values and sqrt
sd = math.sqrt(x/len(stat_values))
print("Std.dev:", f'{sd:.3f}')

#7. median 
#a. sort - do I need to do it more than once?
stat_values.sort()
#b. check if even or odd 
#c. if even add and divide 
#if odd that is the output 
mid = len(stat_values) // 2 #makes things easier
if len(stat_values) % 2 == 0 :
	#idk what to do here - how to identify the two middle numbers 
	median = (stat_values[mid] + stat_values[mid +1]) / 2
else : 
	median = stat_values[mid]
print("Median:", f'{median:.3f}')


"""
python3 stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
