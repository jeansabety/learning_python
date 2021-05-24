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

#translate dictionary 
gcode = {
	'AAA' : 'K',	'AAC' : 'N',	'AAG' : 'K',	'AAT' : 'N',
	'ACA' : 'T',	'ACC' : 'T',	'ACG' : 'T',	'ACT' : 'T',
	'AGA' : 'R',	'AGC' : 'S',	'AGG' : 'R',	'AGT' : 'S',
	'ATA' : 'I',	'ATC' : 'I',	'ATG' : 'M',	'ATT' : 'I',
	'CAA' : 'Q',	'CAC' : 'H',	'CAG' : 'Q',	'CAT' : 'H',
	'CCA' : 'P',	'CCC' : 'P',	'CCG' : 'P',	'CCT' : 'P',
	'CGA' : 'R',	'CGC' : 'R',	'CGG' : 'R',	'CGT' : 'R',
	'CTA' : 'L',	'CTC' : 'L',	'CTG' : 'L',	'CTT' : 'L',
	'GAA' : 'E',	'GAC' : 'D',	'GAG' : 'E',	'GAT' : 'D',
	'GCA' : 'A',	'GCC' : 'A',	'GCG' : 'A',	'GCT' : 'A',
	'GGA' : 'G',	'GGC' : 'G',	'GGG' : 'G',	'GGT' : 'G',
	'GTA' : 'V',	'GTC' : 'V',	'GTG' : 'V',	'GTT' : 'V',
	'TAA' : '*',	'TAC' : 'Y',	'TAG' : '*',	'TAT' : 'Y',
	'TCA' : 'S',	'TCC' : 'S',	'TCG' : 'S',	'TCT' : 'S',
	'TGA' : '*',	'TGC' : 'C',	'TGG' : 'W',	'TGT' : 'C',
	'TTA' : 'L',	'TTC' : 'F',	'TTG' : 'L',	'TTT' : 'F',
}
	
#translate: 
def translate(seq): 
	seq = seq.upper() #normalize upper and lowercase letters 
	protein = ''
	for i in range(0, len(seq) -2, 3): #each codon
		#protein += gcode[seq[i:i+3]]
		codon = seq[i:i+3] 
		if codon in gcode: 
			protein += gcode[codon] #if codon in dict, use it
		else : 
			protein += 'X' #any weird codon will become an X
	return protein
	

#reverse compliment: 
def rc(seq): 
	rcdna = ''
	for i in range(len(seq) -1, -1, -1) : 
		nt = seq[i] 
		if   nt == 'A' : nt = 'T'
		elif nt == 'T' : nt = 'A'
		elif nt == 'C' : nt = 'G' 
		elif nt == 'G' : nt = 'C'
		else           : nt = 'N' 
		rcdna += nt
	return rcdna

#ORF but prints the dna seq rather than the length: 
def orfseq(seq): 
#find ATG
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
			if stop != None: yield seq[start:stop] #yield returns one at a time - doesnt create the whole list, does one at a time 
	
		