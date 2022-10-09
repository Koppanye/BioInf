with open("revc_test", "r") as fájl:
    dna = fájl.read()
    rev = []
    for i in range(len(dna)-1, -1,-1):
        if dna[i] == 'A':
            rev.append('T')
        elif dna[i] == 'T':
            rev.append('A')
        elif dna[i] == 'G':
            rev.append('C')
        elif dna[i] == 'C':
            rev.append('G')
print(''.join(rev))