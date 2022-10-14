def fasta_reader(s):
    with open(s, 'r') as fájl:
        inpt = fájl.read().split('\n')
        dikt = {}
        prev = ''
        for s in inpt[:-1]:
            if s[0] == '>':
                s = s[1:]
                dikt[s] = ''
                prev = s
            else:
                dikt[prev] += s
        return dikt

def gc_content(s):
    return len([i for i in s if i == 'G' or i == 'C']) / len(s) * 100