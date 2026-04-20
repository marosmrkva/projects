n = int(input())
sachovnice = []
for i in range(n):
    r = input().split()
    sachovnice.append(r) #[['...'], ['...'], ['...']]

tabulka = []
for i in range (n):
    s = n*[False]
    tabulka.append(s)

print(tabulka)

vyuziteradky = []
vyuzitesloupky = []
reseni = 0

def rozestaveni (n):
    if n == 0:
        global reseni
        reseni += 1
    for i in range (n):
        print("i,", i)
        for j in range (n):
            print("j,", j)
            if sachovnice[i][j] == "." and tabulka[i][j] == False:
                n-=1
                tabulka [i] = True
                for k in range(n):
                    tabulka [i][j] == True
    rozestaveni (n)
    return 
rozestaveni(n)
print (reseni)