#complexity filter 

import mcb185 
import argparse 
import math 

#import fasta file, set default window length and default complexity level, switch for AA
parser = argparse.ArgumentParser(description='complexity filter')
# required arguments
parser.add_argument('--fasta', required=True, type=str, 
	metavar='<str>', help='required fasta file')
# optional arguments with default parameters
parser.add_argument('--window', required=False, type=int, default=15,
	metavar='<int>', help='window size [%(default)s]')
parser.add_argument('--threshold', required=False, type=float, default=1.1, 
	metavar='<float>', help='threshold [%(default)i]')
parser.add_argument('--amino_acid', action='store_true',
	help='use when using an amino acid sequence, change the threshold')
# finalization
arg = parser.parse_args()

#change threshold for AA 
#if arg.amino_acid: arg.threshold == 2

#empty string so I don't overide the genome --> runs in parallel 
seq2=''
for name, seq in mcb185.read_fasta(arg.fasta): 

	seq.upper() #make input uppercase 
	
	for i in range(len(seq) - arg.window +1): #create window in which entropy is calculated 
		win = seq[i:i+arg.window] 

		nt = {} #create dict that counts how many times each nt was seen 
		for c in win: 
			if c not in nt: nt[c] = 1 #if we haven't seen it before --> 1
			else: nt[c] += 1 

		count = nt.values() #create a list of all the values 
		prob = []
		for v in count: 
			prob.append(v/arg.window) #divide vales by the window size 

		h = mcb185.entropy(prob)
		if h >= arg.threshold: 
			seq2 += seq[i]
		else: 
			seq2 += seq[i].lower()
			
	print(f'>{name}') 
	for i in range(0, len(seq2), 80):
			print(seq2[i:i+80])


