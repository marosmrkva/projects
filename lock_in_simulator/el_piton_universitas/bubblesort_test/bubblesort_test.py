def bubbleSort_1(a):
    n = len(a)                  # delka vstupu
    
    posledni_zamena = n - 1     # kde v poslednim pruchodu polem nastala posedni zamena
    while posledni_zamena > 0:  # prevede (n-i)-te maximum
        
        hranice, posledni_zamena = posledni_zamena, -1
        
        for j in range(hranice):     # na pozici (posledni_zamena -1) od konce 
            print(f"{j=}")
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                posledni_zamena = j
        print(f"{posledni_zamena=}")
        print(a)


pole  = [10, 50, 30, 20, 80, 40, 90, 60]
bubbleSort_1(pole)
