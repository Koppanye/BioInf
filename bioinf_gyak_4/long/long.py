import sys, os
dn = os.path.dirname(__file__)
pdn = os.path.join(dn, "..")
sys.path.append(pdn)

from utils import fasta_reader

dnas = fasta_reader('long_test')
dna_rosa = list(dnas.keys())
dna_strings = list(dnas.values())

def overlap(s,t):
    return max([k for k in range(len(s)) if s[-k:] == t[:k] or k == 0])

#print(dna_strings)
sorrend = []
c = len(dna_strings)
while len(dna_strings) != 0:
    for u in dna_strings:
        d = [i for i in dna_strings if overlap(i,u) > max(len(i), len(u))]
        if len(d) == 0:
            sorrend.append(u)
            dna_strings.remove(u)

s = sorrend[0]
for i in range(1, len(sorrend)):
    s += sorrend[i][overlap(sorrend[i-1], sorrend[i]):]
print(s)






