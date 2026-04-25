import sys
from collections import deque #obojstranna fronta (double-ended queue)

def kral():
    vstup = sys.stdin.read().split() #nacita cely vstup kym uzivatel neoznami koniec
    if not vstup:
        return #nemoze byt prazdny
    it = iter(map(int, vstup)) #musi to byt iterable aby sme vedeli lepie pracovat s prvkami

    try:
        pocet_prekazok = next(it) #prve cislo je pocet
        prekazky = set() #set = mnozina suradnic
        for _ in range(pocet_prekazok):
            ox, oy = next(it), next(it)
            prekazky.add((ox, oy)) #postupne sa posuvame cez cisla a pridavame zadany pocet medzi suradnice
        start = (next(it), next(it)) #po suradniciach dalsi je start
        ciel = (next(it), next(it)) #po starte ciel

    except StopIteration:
        return #vrati ked dojdu cisla

    fronta = deque([(start[0], start[1], [start])]) #vytvorime si frontu pre cestu
    prejdene = set([start]) #sem zapisujeme prejdete policka, teda kam sa uz nechceme vracat
    prejdene.update(prekazky) #prekazky mozeme brat ako prejdene, kedze ani tam neeme ist, pridame do mnoziny suradnic prejdenych (zakazanych) policok

    while fronta: #kym je nieco vo fronte
        x, y, cesta = fronta.popleft() #lavy prvok fronty

        if (x, y) == ciel: #kontrola ci sme v cieli
            for px, py in cesta:
                print(f"{px} {py}") #vypiseme cestu
            return #funkcia konci

        for dx in [-1, 0, 1]: #vsetky tahy kralom po osi x
            for dy in [-1, 0, 1]: #vsetky tahy kralom po osi y
                if dx == 0 and dy == 0: #ak stojime na mieste nic sa nestane, pokracujeme dalej
                    continue
                nx, ny = x+dx, y+dy #zmenime poziciu krala
                if 1 <= nx <= 8 and 1 <= ny <= 8 and (nx, ny) not in prejdene: #kontrola ci sme este na sachovnici a ci nie sme v prekazke
                    prejdene.add((nx, ny)) #oznacime ako prejdene
                    fronta.append((nx, ny, cesta + [(nx, ny)])) #upravime cestu vo fronte
                    
    print("-1") #ak nenajdeme cestu

if __name__ == "__main__":
    kral()