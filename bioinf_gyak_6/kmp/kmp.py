from utils import fasta_reader

def overlap(t):
    return max([i for i in range(len(t)-1) if t[:i] == t[-i:] or i == 0])


s = list(fasta_reader("kmp_test_2").values())[0]
n = len(s)

pref = {i: [""] for i in range(n)}
for k in range(1, n):
    for szo in pref[k-1]:
        if szo + s[k] == s[:len(szo)+1]:
            pref[k].append(szo + s[k])

err = []
for k in range(n):
    err.append(max([len(szo) for szo in pref[k]]))

print(*err)
