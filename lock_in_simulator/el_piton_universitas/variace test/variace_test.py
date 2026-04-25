from itertools import variations

pocetminci = int(input())
mince = input().split()
for i in range(pocetminci):
    mince[i] = int(mince[i])
suma = int(input())

for v in variations(mince):
    
        