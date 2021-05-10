#!/usr/bin/env python3

import sys

# Write a program that predicts if a protein is trans-membrane
# Trans-membrane proteins have the following properties
#	Signal peptide: https://en.wikipedia.org/wiki/Signal_peptide
#	Hydrophobic regions(s): https://en.wikipedia.org/wiki/Transmembrane_protein
#	No prolines in hydrophobic regions (alpha helix)
# Hydrophobicity is measued via Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot
# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa

#1. function for kd hydrophobicity 
#for each AA, add it's value to a total and divide by the number of AA
def kd(seq): #kd = kite-doolittle = way of calc hydropho
	kdsum = 0 #should this go here? 
	for i in range(len(seq)): 
		if seq[i] == 'I'   : kdsum += 4.5
		elif seq[i] == 'V' : kdsum += 4.2
		elif seq[i] == 'L' : kdsum += 3.8
		elif seq[i] == 'F' : kdsum += 2.8
		elif seq[i] == 'C' : kdsum += 2.5
		elif seq[i] == 'M' : kdsum += 1.9
		elif seq[i] == 'A' : kdsum += 1.8
		elif seq[i] == 'G' : kdsum -= 0.4
		elif seq[i] == 'T' : kdsum -= 0.7
		elif seq[i] == 'S' : kdsum -= 0.8
		elif seq[i] == 'W' : kdsum -= 0.9
		elif seq[i] == 'Y' : kdsum -= 1.3
		elif seq[i] == 'P' : kdsum -= 1.6 #what do I do about the proline? 
		elif seq[i] == 'H' : kdsum -= 3.2
		elif seq[i] == 'E' : kdsum -= 3.5
		elif seq[i] == 'Q' : kdsum -= 3.5
		elif seq[i] == 'D' : kdsum -= 3.5
		elif seq[i] == 'N' : kdsum -= 3.5
		elif seq[i] == 'K' : kdsum -= 3.9
		elif seq[i] == 'R' : kdsum -= 4.5
	return kdsum/len(seq)
#this doesn't work 

#2. function that checks for a proline 
def proline(seq): 
	for c in seq: 
		if c == 'P' : return True 
		else 		: pass
#print(kd('R'))

#2. get all the sequences: 
proteins = [] #sequences
ids = [] #name of the proteins 

with open(sys.argv[1]) as fp:  #put file name in command line - python3 Work/learning_python/classwork.py
	seq = [] #sequence of AA - here so we can look at one sequence at a time 
	for line in fp.readlines(): #read every line
		line = line.rstrip() 
		if line.startswith('>'): #this is the standard beginning of a  new section/definition (new protein + seq in this case )
			words = line.split() #lets you collect multiple lines of sequence, as many lines needed until next >
			ids.append(words[0][1:])
			if len(seq) > 0 : proteins.append(''.join(seq)) 
			seq = [] #now know what each sequence is 
		else : #if it doesn't start with >, it is a sequence ...
			seq.append(line) #...so add that line to seq
	proteins.append(''.join(seq)) #add your sequence (made from mashing the lines between >) to proteins 
	


#3. look for hydrophobic regions in all sequences 
w = 11
s = 8
for id, seq in zip(ids, proteins): #go through ids and proteins together 
	#calculate hydrophobicity 
	hd_region = False
	sig_pep = False
	for i in range(len(seq[29:]) - w + 1 ) : 
		pep = seq[i:i+w]
		if kd(pep) > 2 and not proline(pep) : hd_region = True
		#print(i, kd(seq[i:i+w]))
	for i in range(len(seq[:29]) - s + 1)  : 
		if kd(pep) > 2.5 : sig_pep = True
		#print(sig_pep)
	#want to say if they are both true
	if hd_region == True and sig_pep == True : print(id) #could say hd_region and sig_pep - check itself, and is a boolean 
	
#also tried .append 
#can use 'in' to ask if something is in your sequence 
"""
python3 Programs/transmembrane.py Data/at_prots.fa
AT1G75120.1
AT1G10950.1
AT1G75110.1
AT1G74790.1
AT1G12660.1
AT1G75130.1
"""
