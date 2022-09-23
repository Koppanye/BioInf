with open("ini6", "r") as szoveg:
    tartalom = szoveg.read().split(" ")
    szavak = {}
    for szo in tartalom:
        if szo not in szavak.keys():
            szavak[szo] = 1
        else:
            szavak[szo] += 1
    for key,value in szavak.items():
        print(key,value)