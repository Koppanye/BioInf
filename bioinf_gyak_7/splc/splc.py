from utils import fasta_reader, dna_to_prot, dna_to_rna

c = fasta_reader("splc_test_2")
s = list(c.values())[0]
print(s)
introns = list(c.values())[1:]

for t in introns:
    s = s.replace(t, "")
print(s)
print(dna_to_prot(dna_to_rna(s)))


