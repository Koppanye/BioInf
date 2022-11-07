with open("asmq_test", "r") as f:
    l = []
    line = f.readline()
    while line:
        l.append(line.strip())
        line = f.readline()

    lsum = sum([len(i) for i in l])
    maxlen = max([len(i) for i in l])
    lista = [sum([len(s) for s in l if len(s) >= i]) for i in range(1, maxlen + 1)]

    fifty = max([i for i in range(maxlen) if lista[i] / lsum >= 0.5]) + 1
    seventyfive = max([i for i in range(maxlen) if lista[i] / lsum >= 0.75]) + 1

    print(lista)
    print(maxlen)
    print(fifty, seventyfive)