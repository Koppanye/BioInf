def fasta_reader(s):
    with open(s, 'r') as fájl:
        input = fájl.read().split('\n')
        szotar = {}
        prev = ''
        for s in input[:-1]:
            if s[0] == '>':
                s = s[1:]
                szotar[s] = ''
                prev = s
            else:
                szotar[prev] += s
        return szotar

def gc_content(s):
    return len([i for i in s if i == 'G' or i == 'C']) / len(s) * 100

parok = fasta_reader('gc_test')

lista = sorted(list(parok.keys()), key = lambda x: gc_content(parok[x]), reverse = True)
print(lista[0])
print(gc_content(parok[lista[0]]))





