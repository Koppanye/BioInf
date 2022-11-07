from itertools import permutations as p
with open("perm_test") as f:
    n = int(f.read().strip())
    perms = list(p(range(1, n+1)))
    print(len(perms))

    for i in perms:
        print(*i)