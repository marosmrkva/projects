vstup = input().split()
pocet, zaciatok = int(vstup[0]), int(vstup[1])

domino = input().split()
kocky = [(int(x[0]), int(x[1])) for x in domino]

najlepsi = []
aktualny = []
pouzite = [False] * pocet
vysledok = []

kocky_mozne = [[] for _ in range(7)]
for i, (a,b) in enumerate(kocky):
    kocky_mozne[a].append(i)
    if a != b:
        kocky_mozne[b].append(i)

def backtrack(hodnota):
    global najlepsi

    if len(aktualny) + (pocet - sum(pouzite)) <= len(najlepsi):
        return

    if len(aktualny) > len(najlepsi):
        najlepsi = aktualny[:]

    for i in kocky_mozne[hodnota]:
        if not pouzite[i]:
            a, b = kocky[i]
            
            pouzite[i] = True

            aktualny.append((a,b) if hodnota == a else (b,a))
            backtrack(b if hodnota == a else a)
            aktualny.pop()
            
            pouzite[i] = False



backtrack(zaciatok)

print(len(najlepsi))

for a, b in najlepsi:
    vysledok.append((str(a) + str(b)).strip())
    
print(" ".join(vysledok))