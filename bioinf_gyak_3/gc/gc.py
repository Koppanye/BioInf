import sys, os
dn = os.path.dirname(__file__)
pdn = os.path.join(dn,"..")
sys.path.append(pdn)

from utils import fasta_reader, gc_content

parok = fasta_reader('gc_test')

lista = sorted(list(parok.keys()), key = lambda x: gc_content(parok[x]), reverse = True)
print(lista[0])
print(gc_content(parok[lista[0]]))

import networkx as nx
print(nx)






