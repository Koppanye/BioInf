from utils import fasta_reader

dnas = list(fasta_reader("cons_test_2").values())


a = [0 for _ in range(len(dnas[0]))]
c = [0 for _ in range(len(dnas[0]))]
g = [0 for _ in range(len(dnas[0]))]
t = [0 for _ in range(len(dnas[0]))]

for item in dnas:
    for i in range(len(item)):
        if item[i] == "A":
            a[i] += 1
        elif item[i] == "C":
            c[i] += 1
        elif item[i] == "G":
            g[i] += 1
        elif item[i] == "T":
            t[i] += 1

cons = ""
for i in range(len(a)):
    maxi = max([a[i], c[i], g[i], t[i]])
    if maxi == a[i]:
        cons += "A"
    elif maxi == c[i]:
        cons += "C"
    elif maxi == g[i]:
        cons += "G"
    elif maxi == t[i]:
        cons += "T"
print(cons)
print("A: ", *a)
print("C: ", *c)
print("G: ", *g)
print("T: ", *t)




