"""
cislo = int(input())
kandidat = 2
while (kandidat*kandidat <= cislo):
    if (cislo%kandidat == 0):
        print(kandidat)
        cislo //= kandidat
    else:
        kandidat += 1
print(kandidat) 


import time 
import random

a = []
for i in range (1000000):
    a.append(f"beer nr. {i+1}")

for i in range (100):
    print(random.choice(a))
    time.sleep(1)



a = "nazdar"
obracene = ""
for i in range(len(a)):
    obracene = a[i] + obracene
print(obracene)


a = [[2,4,6], [1,[7,9],5]]

print(a[1][1][1])
print(a)
a[1][1].append(11)

print(a[1][1][2])

for i in range(len(a)):
    print(i, end=" ")
"""




def secti (a,b,c):
    d=a+b+c
    return d 
print (secti (8,2,3))