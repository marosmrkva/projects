vstup = None

ingrediencie = []
mnozstva = []

while vstup != [""]:
    vstup = input().split(":")
    if "-" in vstup[0]:
        vstup[1] = vstup[1].split()
        if vstup[0][2:] not in ingrediencie:
            ingrediencie.append(vstup[0][2:])
            mnozstva.append([int(vstup[1][0]), vstup[1][1]])
        elif vstup[0][2:] in ingrediencie:
            mnozstva[ingrediencie.index(vstup[0][2:])][0] += int(vstup[1][0])

ingrediencie_sort = sorted(ingrediencie[:])
mnozstva_sort = []
for i in ingrediencie_sort:
    mnozstva_sort.append(mnozstva[ingrediencie.index(i)])

for i in range(len(ingrediencie)):
    if "g" in mnozstva_sort[i] and mnozstva_sort[i][0] >= 1000: 
        mnozstva_sort[i][1] = "kg" 
        mnozstva_sort[i][0] = round(mnozstva_sort[i][0]/1000, 1) 
    mnozstva_sort[i][0] = str(mnozstva_sort[i][0])
    print(ingrediencie_sort[i]+":", " ".join(mnozstva_sort[i])) 