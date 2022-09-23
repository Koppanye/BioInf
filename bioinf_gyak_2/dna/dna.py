with open("dna_text", "r") as fájl:
    dna = fájl.read().strip()
    chars = {"A":0, "C":0, "G":0, "T":0}
    for char in dna:
        chars[char] += 1
    for char in chars.keys():
        print(chars[char])