N = input()
pocet = 0

for i in range(int(N)):
    pocetdelitelov = 0
    number = (i+1)

    for j in range(len(str(number))):
        indexj = (int(str(number)[j]))
        if indexj != 0 and number % indexj == 0:
            pocetdelitelov += 1

    if pocetdelitelov == len(str(number)):
        pocet += 1

print(pocet)
