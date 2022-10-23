from utils import rev_comp
with open("revc_test_2", "r") as f:
    dna = f.read()
    print(rev_comp(dna))