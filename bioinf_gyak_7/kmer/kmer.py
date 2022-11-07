from utils import fasta_reader
from itertools import product as p

c = 4
s = list(fasta_reader("kmer_test_3").values())[0]

kmers = p("ACGT", repeat = c)
kmercomp = {"".join(t): 0 for t in kmers}

for i in range(len(s)-(c-1)):
    kmercomp[s[i:i+4]] += 1

print(*kmercomp.values())
#print(*[str(i) for i in kmercomp.values()])
