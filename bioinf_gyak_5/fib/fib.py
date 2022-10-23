with open("fib_test_2", "r") as f:
    val = f.read().split()
    n, k = int(val[0]), int(val[1])

    l = [1,1]
    for i in range(n-2):
        l.append(l[-1] + k * l[-2])
    print(l[-1])
