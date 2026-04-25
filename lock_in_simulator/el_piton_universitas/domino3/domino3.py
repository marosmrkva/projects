vstup = input().split()
pocet, zaciatok = int(vstup[0]), int(vstup[1])

domino = input().split()
kocky = []
for i in domino:
    for j in i:
        kocky.append(int(j)) #vsetky vstupy spracovane

tabulka = [[0]*7 for i in range(7)]

for i in range(0, 2*pocet, 2): #tabulka pocita roztriedene ostavajuce kocky
    a = kocky[i]
    b = kocky[i+1]
    x = min(a,b)
    y = max(a,b)
    tabulka[x][y] += 1

najlepsiadlzka = 0
najlepsi = []
aktualny = []
vysledok = []

def backtrack(hodnota, dlzka):
    global najlepsi, najlepsiadlzka

    if len(aktualny) > len(najlepsi):
        najlepsiadlzka = dlzka
        najlepsi = aktualny[:]

    for i in range(7):
        x = min(hodnota, i)
        y = max(hodnota, i)

        if tabulka[x][y] > 0:
            tabulka[x][y] -= 1
            aktualny.append((hodnota, i))
            backtrack(i, dlzka+1)
            aktualny.pop()
            tabulka[x][y] += 1



backtrack(zaciatok, 0)

print(len(najlepsi))

for a, b in najlepsi:
    vysledok.append((str(a) + str(b)).strip())
    
print(" ".join(vysledok))

