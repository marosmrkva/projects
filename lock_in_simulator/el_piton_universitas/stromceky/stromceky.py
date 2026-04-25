import os
import random
clear = lambda: os.system('cls')

les = []

for i in range(200):
    riadok = []
    for j in range(170):
        riadok.append(".")
    les.append(riadok)

def lesupdate(les):
    clear()
    for i in range(len(les)-1, 0, -1):
        print(les[i])
lesupdate(les)

def trojuholnik(vyska, x, y):
    for j in range(vyska+1):
        for i in range(x-j+1, x+j, 1):
            bod(i, y, "0", les)
        y -= 1

def bod(x, y, znak, les):
    les[y][x] = znak

def strom(x, y, d, les, znak):
    length = 0
    for i in range(d): #kmen
        bod(x, y, znak, les)
        y+=1
        length += 1
        if length == d:
            break
    trojuholnik(5, x, y+d)
    trojuholnik(5, x, y+d+4)
    trojuholnik(4, x, y+d+7)

wait = input()
for i in range(150):
    x = random.randint(5, 165)
    y = random.randint(0, 185)
    strom(x, y, 4, les, "0")
    lesupdate(les)