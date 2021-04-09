#!/usr/bin/env python3

# Write a program that computes the running sum from 1..n
# Also, have it compute the factorial of n while you're at it
# No, you may not use math.factorial()
# Use the same loop for both calculations

n = 5

sum=0
fac=1 #need to start at one or we will multiply by zero every time we go through the loop 
for i in range(1, n+1):
	sum=sum+i #sum changes every time we go through the loop
	fac=fac*i 
print(sum, fac)

"""
python3 sumfac.py
5 15 120
"""
