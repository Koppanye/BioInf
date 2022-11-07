with open("seto_test_3", "r") as f:
    n = int(f.readline().strip())
    A = f.readline().strip()[1:-1].split(",")
    B = f.readline().strip()[1:-1].split(",")

    A = [int(i) for i in A]
    B = [int(i) for i in B]

    print(set([i for i in A] + [i for i in B]))
    print(set([i for i in A if i in B]))
    print(set([i for i in A if i not in B]))
    print(set([i for i in B if i not in A]))
    print(set([i for i in range(1, n + 1) if i not in A]))
    print(set([i for i in range(1, n + 1) if i not in B]))