import sys, os
dn = os.path.dirname(__file__)
pdn = os.path.join(dn, "..")
sys.path.append(pdn)

from utils import fasta_reader
import networkx as nx

dnas = fasta_reader('long_test')
dna_rosa = list(dnas.keys())
dna_strings = list(dnas.values())

def overlap(s,t):
    return max([k for k in range(len(s)) if s[-k:] == t[:k] or k == 0])

G = nx.DiGraph()
G.add_nodes_from(dna_strings)

for u in G.nodes():
    for v in G.nodes():
        if overlap(u,v) > max(len(u) / 2, len(v) / 2):
            G.add_edge(u,v)

sort_nodes = sorted(G.nodes, key = lambda x: G.out_degree(x))
v = sort_nodes[0]
u = list(G.successors(v))[0]
k = overlap(v,u)
G.add_edge(v + u[k:], list(G.successors(u))[0])
G.remove_node(v)
G.remove_node(u)
print(G.edges(), G.nodes())


for i in range(len(G.nodes()-1)):
    sort_nodes = sorted(G.nodes, key = lambda x: G.out_degree(x))
    v = sort_nodes[0]
    u = list(G.successors(v))[0]
    k = overlap(v,u)
    G.add_edge(v + u[k:], list(G.successors(u))[0])
    G.remove_node(v)
    G.remove_node(u)



