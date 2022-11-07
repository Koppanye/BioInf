import networkx as nx

with open("tree_test_2", "r") as f:
    fajl = f.readlines()
    n = int(fajl[0].strip())
    print(n-len(fajl))