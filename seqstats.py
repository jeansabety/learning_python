import argparse 
import mcb185 
import statistics 

parser = argparse.ArgumentParser(description='stats about sequence')
# required arguments
parser.add_argument('--file', required=True, type=str, #--r1 = string 
	metavar='<str>', help='required fasta file')
arg = parser.parse_args() 

#add all the sequence lengths to a list: 
length = []
for name, seq in mcb185.read_fasta(arg.file) : 
	#print(name, len(seq))
	length.append(len(seq))

length.sort()

print('min is', min(length))
 
print('max is', max(length))

#sum: 
#sum = 0
#for value in length: 
#	sum += value 
print('sum is', sum(length))

print('mean is', statistics.mean(length))

print('median is', statistics.median(length))

print('n50 is', mcb185.n50(length))

#or: 
#def n50(length) : 
#	length.sort()
#	running_sum = 0 
#	total = sum(length)
#	i = 0
#	while running_sum < total/2 : 
#		running_sum += length[i]
#		i += 1
#	return length[i]