from utils import rev_comp
with open("dbru_test_2", "r") as f:
    l = []
    line = f.readline()
    while line:
        if line.strip() not in l:
            l.append(line.strip())
        line = f.readline()

    for kmer in l:
        if rev_comp(kmer) not in l:
            l.append(rev_comp(kmer))

    for kmer in l:
        a, b = kmer[:-1], kmer[1:]
        print("(" + a + ", " + b + ")")