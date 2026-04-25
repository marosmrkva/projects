pocet = int(input())
mince = list(map(int, input().strip().split()))
suma = int(input())

vysledok = []

if 0 in mince:
    mince.pop(mince.index(0))

def mincovka(index, zvysok, output):
    if zvysok == 0:
        print(*output)
        return
    if index == pocet:
        return

    minca = mince[index]
    pocet_max = zvysok//minca

    for i in range(pocet_max, -1, -1):
        zvysok_novy = zvysok - i * minca
        output_novy = output + [minca] * i
        mincovka(index+1, zvysok_novy, output_novy)

mincovka(0, suma, [])


for i in vysledok:
    print(*i)   

