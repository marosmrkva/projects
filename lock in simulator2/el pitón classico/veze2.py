velkost = int(input())

sachovnica = []
for i in range(velkost):
    riadok = input()
    riadok_list = []
    for j in range(velkost):
        riadok_list.append(riadok[j])
    sachovnica.append(riadok_list)

print(sachovnica)

"""

3   -----> velkost

. . .
. X .
. . .

"""
#i = 0
#riadky = []
#pouziteveze = 0
#velkost = 3


def veze (pouziteveze, riadky):   

    if pouziteveze == velkost:
        return 1
    
    pocetmoznosti = 0

    for i in range(velkost):
        if sachovnica[i][pouziteveze] != "X" and i not in riadky:
            riadky.append(i)
            pocetmoznosti += veze(pouziteveze+1, riadky)
            riadky.pop(riadky.index(i))
