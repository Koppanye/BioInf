fájl = open("ini5_text", "r")
i = 1
for line in fájl:
  if i % 2 == 0:
    print(line)
  i += 1
fájl.close()
