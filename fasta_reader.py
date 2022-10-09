def fasta_reader(s):
    with open(s, 'r') as fájl:
        input = fájl.read().split('\n')
        dict = {}
        prev = ''
        for s in input[:-1]:
            if s[0] == '>':
                s = s[1:]
                dict[s] = ''
                prev = s
            else:
                dict[prev] += s
        return dict