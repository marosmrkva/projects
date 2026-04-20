a = [2,8,5,8,0,0,7,2,0,20]
b = [10,8,20,0,2,2,10,7]
a.sort()
b.sort()

#a = [0, 0, 0, 2, 2, 5, 7, 8, 8, 20]
#b = [0, 2, 2, 7, 8, 10, 10, 20]

def reseni(a,b):
    c = []
    i = 0
    j = 0
    # dokud je ty jezdce kam posouvat
    while i != len(a) - 1 or j != len(b) - 1:
        # porovnani poctu stejnych prvku
        if a[i] == b[j]:
            pocet_a = 0
            pocet_b = 0
            prvek = a[i]
            # po tomhle budou i,j ukazovat na nejblizsi prvky za tim, na ty, co se uz lisi
            while a[i] == prvek:
                pocet_a += 1
                i += 1
            while b[j] == prvek:
                pocet_b += 1
                j += 1
            # a kdyz uz to mame spoctene, tak pridani tolikrat, co nam rika zadani
            for _ in range(abs(pocet_a - pocet_b)):
                c.append(prvek)
        else:
            # muzeme udelat diky tomu, ze mame oba seznamy serazene
            # proste prvky co jsou jenom v jednom seznamu vypiseme a pricitame ten index
            # pokud takovych prvku bude vic, tak se v dalsi iteraci while sem dostaneme znova
            # a to az do chvile, co se ty prvky zase nezacnou shodovat 
            # (coz pokud prvky spolecne seznamum a,b jeste jsou, tak musi znovu nastat diky razeni, zadne prvky nezapomeneme)
            if a[i] < b[j]:
                c.append(a[i])
                i += 1
            elif b[j] < a[i]:
                c.append(b[j])
                j += 1
    print(c)

reseni(a,b)



