
from multiprocessing.managers import ListProxy


a = 3
b = 8
# vytvor seznam s cisel a,a+1,...,b
# s pouzitim cyklu
s = []
for i in range(a, b+1):
    s.append(i)
print(s)

# bez cyklu (list comprehension)


# pridej na konec cislo 9
s.append(9)
print(s)

# pridej na zacatek cislo 2
s.insert(0, 2)
print(s)

# pridej na konec cisla 10, 11, 12
s.extend([10, 11, 12])
print(s)

# pridej na zacatek cisla -2, -1, 0
s = [-2, -1, 0] + s
print(s)

# vynech cislo 5
s.pop(6)
print(s)
# vynech cislo na pozici 3 (pocitano od nuly)
s.pop(s[4])
print(s)

# vynech vsechna suda cisla
for i in s:
    if i%2 == 0:
        s.pop(s.index(i))
print(s)

# vynasob vsechna cisla cislem 3
s = [i*3 for i in s]
print(s)

# vlozte cislo 22 mezi 21 a 24
s.insert(s.index(21)+1, 22)
print(s)

k = 4
# vypiste prvnich k cisel
print(s[:k])

# vypiste poslednich k-2 cisel
print(*s[-(k-2):])

# otocte seznam / cyklem
s1 = []
for i in range(len(s)):
     s1 = s1 + [s[-i-1]]
s = s1
print(s)

# otocte seznam - bez cyklu
s = s[::-1]
print(s)

# dale implementujte funkce
# funkce, ktera slepi mdva seznamy do jednoho
def zlepit (s1, s2):
    return(s1 + s2)
s = zlepit(s, s1)
print(s)

# funkce, ktera udela prunik dvou seznamu
def prienik (s1, s2):
    s = []
    for i in s2:
        if i in s2:
            s.append(i)
    return(sorted(s))

prienikzoznamov = prienik(s, s1)
print(prienikzoznamov)

# funkce, ktera udela rozdil dvou seznamu

# funkce, kter8 vyh8z9 duplicitn9 prvky

# funkce, ktera sleje dva setridene seznamy do jednoho

# mame seznam seznamu [['mleko', 'maslo'],['mleko', 'syr'], ...]
# funkce, ktera vypise ruzne prvky ze vsech seznamu

#               pocty prvku ve vsech seznamech
