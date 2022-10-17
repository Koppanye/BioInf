with open("subs_test_2", "r") as f:
    s = f.readline()
    t = f.readline()
    indices = ""
    for i in range(0, len(s)-len(t)):
        if s[i:i + len(t)] == t:
            indices += (str(i+1) + " ")
    print(str(indices))