import time

vstup = list(map(int, input().strip().split()))

def najdi_max(vstup):
    if not vstup:
        return None

    pocet_vyskytov = {}
    for x in vstup:
        pocet_vyskytov[x] = pocet_vyskytov.get(x, 0) + 1


    aktualny_max = -float("inf")
    index_max = -1

    for i in range(len(vstup)):
        prvok = vstup[i]
        if pocet_vyskytov[prvok] == 1:
            if prvok > aktualny_max:          
                aktualny_max = vstup[i]
                index_max = i


    return [aktualny_max, index_max] if index_max != -1 else None



print(*najdi_max(vstup))









class strom:
    pass

def vypis(koren, zoznam_listov):

    if koren.lavy != None:
        vypis(koren.lavy)

    if koren.pravy != None:
        vypis(koren.pravy)

    if koren.lavy == None and koren.pravy == None:
        zoznam_listov.append(koren.hodnota)
    
    return zoznam_listov


zoznam_listov = vypis(strom, [])