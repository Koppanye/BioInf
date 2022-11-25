from utils import pcov
with open("pcov_test_2", "r") as f:
    l = []
    line = f.readline()
    while line:
        if line.strip() not in l:
            l.append(line.strip())
        line = f.readline()

    v = pcov(l)
    print(v)