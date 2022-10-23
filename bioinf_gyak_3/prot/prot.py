from utils import dna_to_prot

with open("prot_test", "r") as f:
    s = f.read().strip()
    print(dna_to_prot(s))



