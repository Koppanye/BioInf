from utils import fasta_reader, dna_to_prot, rev_comp, dna_to_rna

l = fasta_reader("orf_test_2")
dna1 = list(l.values())[0]
dna2 = dna1[1:-2]
dna3 = dna1[2:-1]
dna4 = rev_comp(dna1)
dna5 = dna4[1:-2]
dna6 = dna4[2:-1]

rna1, rna2, rna3, rna4, rna5, rna6 = dna_to_rna(dna1), dna_to_rna(dna2), dna_to_rna(dna3), dna_to_rna(dna4), dna_to_rna(dna5), dna_to_rna(dna6)
prots = [dna_to_prot(rna1), dna_to_prot(rna2), dna_to_prot(rna3), dna_to_prot(rna4), dna_to_prot(rna5), dna_to_prot(rna6)]

sols = []
for prot in prots:
    while prot.find("M") != -1 and prot.find("Stop", prot.find('M')) != -1:
        k = prot.find("M")
        l = prot.find("Stop", k)
        if prot[k:l] not in sols:
            sols.append(prot[k:l])
        prot = prot[k+1:]

for i in sols:
    print(i)





