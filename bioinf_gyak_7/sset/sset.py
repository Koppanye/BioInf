with open("sset_test", "r") as f:
    n = int(f.readline().strip())
    print(2 ** n % 1000000)