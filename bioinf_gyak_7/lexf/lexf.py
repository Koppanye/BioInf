from itertools import product as p

with open("lexf_test", "r") as f:
    l = f.readline().strip().replace(" ", "")
    n = int(f.readline())
    perms = p(l, repeat = n)
    for t in perms:
        print("".join(t))