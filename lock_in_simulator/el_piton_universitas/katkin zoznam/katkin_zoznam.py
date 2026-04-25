vstup = "."

ingredience = []
mnozstva = []

while vstup != [""]:
    vstup = input().split(":") #["- nazov", "cislo jednotka"]
    if "-" in vstup[0]:
        vstup[1] = vstup[1].split() #["- nazov", ["cislo", "jednotka"]]
        if not vstup[0][2:] in ingredience:
            ingredience.append(vstup[0][2:]) #"nazov"
            mnozstva.append([int(vstup[1][0]), vstup[1][1]]) #[cislo, "jednotka"]
        else:
            mnozstva[ingredience.index(vstup[0][2:])][0] += int(vstup[1][0])

                                          #ingredience = ["hladka mouka", "cukr moucka"]
                                          #mnozstva = [[400, "g"], [140, "g"]]

ingredience_sort = sorted(ingredience[:]) #["cukr moucka", "hladka mouka"]
mnozstva_sort = [] #[]

for i in ingredience_sort: #cukr moucka
    mnozstva_sort.append(mnozstva[ingredience.index(i)])

for i in range(len(ingredience_sort)):
    if "g" in mnozstva_sort[i] and mnozstva_sort[i][0] >= 1000: #[400, "g"]
        mnozstva_sort[i][1] = "kg" #[400, "kg"]
        mnozstva_sort[i][0] = round(mnozstva_sort[i][0]/1000, 1) #[0.4, "kg"]
    mnozstva_sort[i][0] = str(mnozstva_sort[i][0])
    print(ingredience_sort[i]+":", mnozstva_sort[i][0], mnozstva_sort[i][1]) 


