#read file 
def read_fasta(filename):
	name = None
	seq = []
	
	with open(filename) as fp:
		while True:
			line = fp.readline()
			if line == '': break
			elif line.startswith('>'):
				if len(seq) > 0: # now is the time to return name, seq
					yield name, ''.join(seq)
				words = line.split()
				name = words[0][1:]
				seq = []
			else:
				line = line.rstrip()
				seq.append(line)
	yield name, ''.join(seq)

#gc content 
def gc(dna): 
	g = dna.count('G')
	c = dna.count('C')
	return (g + c)/len(dna)

#n50	
def n50(length): 
	for value in length : 
			running_sum += value 
			if running_sum > total/2 : 
				return value
				
#generate random sequence of specified size and gc content 
import random 
def randseq(length, gc) : 
	seq = ''
	for i in range(length): 
		if random.random() < gc:  #has to be based on given gc content 
			seq += random.choice('GC')
		else : seq += random.choice('AT')
	return seq
	
#ORF: 
def orf(seq): 
#find ATG
	lengths = []
	for i in range(len(seq) -2): #all the starting positions we could possibly see 
		start = None 
		stop = None
		if seq[i:i+3] == 'ATG':
			start = i
	#one you find an ATG, you have to go by triplets 
			for j in range(i, len(seq) -2, 3) : #starting at A, through the rest of the sequence, by 3s
				codon = seq[j: j+3] #stop codon starts at j
				if codon == 'TAA' or codon == 'TAG' or codon == 'TGA' : 
					stop = j 
					break 
		if stop != None: lengths.append((stop - start)//3) #only if you find a start,stop pair do you add the orf length to the list | /3 so we get the AA length 	
	return lengths	
		