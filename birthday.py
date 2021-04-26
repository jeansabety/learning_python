#!/usr/bin/env python3

# You are probably well aware of the 'birthday paradox'
# https://en.wikipedia.org/wiki/Birthday_problem
# Let's try simulating it

# You will need a list for the 365 day calendar
# You will need a set number of people (e.g. 25)
# During each 'trial' you do the following
#	Choose a person
#	Git them a random birthday
#	Store it in the calendar
# Once you have stored all birthdays, check to see if any have the same day
# Do this for many trials to see what the probability of sharing a birthday is


import random

people = 25
days = 365 #change back to 365 - smaller number for debugging
trials = 10000 #how many trials we will do (change to 10)
duplication = 0

for i in range(trials) : 
	#create an empty calendar of 0s
	calender = [] #want it here so we get a new calendar every trial
	for j in range(days) : 
		calender.append(0) #add a 0 365 times (each j in loop)

	#fill with random birthdays 
	for j in range(people): 
		birthday = random.randint(0,days-1) #gives a random number - now inclusive
		calender[birthday] +=1 #adds 1 to each day in calendar that aligns with birthday 
		
	#check for duplications 
	for day in calender: 
		if day > 1: 
			duplication += 1
			break #need to end the loop - without this we were adding up each duplicate in each calendar, not how many calenders have duplications
			#once you find one, stop looking
print(duplication, trials, duplication/trials)


#-----pseudo code --------# 
##give people a random bday by choosing a number between 0-364
#then ask if two people got the same birthday -> are any counts>1? 
#then figure out how often that happend - do it again until number becomes stable 
#0. for each trial: 
	#1. create empty calendar - array with a bunch of 0s
	#2. fill it with random birthdays - one birthday for each person
	#3. check for duplicates 
	# x 10 (loop)
	#record how many duplicates 
#report the number of duplications per trial 

#all of these things are inside a loop 


"""
python3 birthday.py
0.571
"""

