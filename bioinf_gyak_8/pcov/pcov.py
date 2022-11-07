from utils import overlap
with open("pcov_test_2", "r") as f:
    l = []
    line = f.readline()
    while line:
        if line.strip() not in l:
            l.append(line.strip())
        line = f.readline()

    sorrend = [l[0]]
    l.remove(l[0])
    while len(l) != 0:
        for i in l:
            if sorrend[-1][1:] == i[:-1]:
                sorrend.append(i)
                l.remove(i)

    k = len(sorrend[0])
    n = len(sorrend)

    v = sorrend[0]
    for i in range(n-k):
        v += sorrend[i+1][-1]
    print(v)