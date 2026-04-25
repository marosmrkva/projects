pocetmiest = int(input().strip())
pocetciest = int(input().strip())

mesta = []
for i in range(1, pocetmiest+1, 1):
    mesta.append(i)

cesty = []
for i in range(pocetciest):
    cesta = tuple(map(int, input().split()))
    cesty.append(cesta)

print(cesty)


skupina1 = []
skupina2 = []

hotovo = False

def test(mesta, cesty):
    global skupina1, skupina2
    if hotovo:
        return
    
    if mesta == []:
        hotovo = True
        return

    


    

