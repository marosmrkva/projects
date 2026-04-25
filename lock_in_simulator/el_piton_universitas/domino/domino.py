vstup = input().split()
pocet = int(vstup[0])
zaciatok = int(vstup[1])

domino = input().split()
kocky = [(int(x[0]), int(x[1])) for x in domino]

najlepsi = []
aktualny = []
pouzite = [False] * pocet

kocky_mozne = [[] for _ in range(7)]
for i, (a, b) in enumerate(kocky):
    kocky_mozne[a].append(i)
    if a != b:
        kocky_mozne[b].append(i)

def backtrack(hodnota):
    global najlepsi

    if len(aktualny) > len(najlepsi):
        najlepsi = aktualny[:]


    for index in kocky_mozne[hodnota]:
        if not pouzite[index]:
            a, b = kocky[index]
            pouzite[index] = True

            if a == hodnota:
                aktualny.append((a,b))
                backtrack(b)
                aktualny.pop()
            if b == hodnota:
                aktualny.append((b,a))
                backtrack(a)
                aktualny.pop()

            pouzite[index] = False

        
backtrack(zaciatok)

print(len(najlepsi))

vysledok = []
for a, b in najlepsi:
    vysledok.append((str(a) + str(b)).strip())
print(" ".join(vysledok))