with open("rna_test", "r") as fájl:
    dna = fájl.read()
    rna = []
    for i in range(len(dna)):
        if dna[i] == 'T':
            rna.append('U')
        else:
            rna.append(dna[i])
print(''.join(rna).strip())
