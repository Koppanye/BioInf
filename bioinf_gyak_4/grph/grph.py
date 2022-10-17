import sys, os
dn = os.path.dirname(__file__)
pdn = os.path.join(dn, "..")
sys.path.append(pdn)

from utils import fasta_reader

k = 3
inpt = fasta_reader('grph_test_2')
vert = list(inpt.keys())
for i in vert:
    for j in vert:
        s = inpt[i]
        t = inpt[j]
        if s != t and s[-3:] == t[:3]:
            print(i + " " + j)


