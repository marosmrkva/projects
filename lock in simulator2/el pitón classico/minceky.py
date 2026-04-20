pocet = int(input()) #klasika vstup, berieme pocet minci = cislo = int()
mince = list(map(int, input().strip().split())) #zoznam minci = zoznam hodnot = chceme zoznam intov = int() = dame na vsetky -> map() = class, chceme list = list()
suma = int(input()) #celkova suma = cislo = int()

if 0 in mince: #0 je zbytocna minca
    mince.pop(mince.index(0)) #vyhodime zo zoznamu, pop vybera podla indexu, zistile index 0 a popneme ten

def mincovka(index, zvysok, output): #zacina funkcia, parametre index = index aktualnej mince v zadanom poli minci, zvysok = kolko nam ostava zaplatit, output = aktualna vysledna kombinacia minci
    if zvysok == 0: #ak je zvysok 0 = nemame co uz platit
        print(*output) #vypiseme co mame vo vysledku
        return #funkcia konci (je to rekurzia takze nekonci cely program, iba jedna funkcia v celej rekurzii)
    if index == pocet: #index = pocet teda presli sme vsetky mince, aktualny index je rovnaky ako pocet minci, ziadne dalsie uz nemame (list ide od 0 po n-1 takze ak index=pocet, sme mimo listu a zastavujeme rekurziu)
        return #funkcia konci (zase iba jedna, nie cely program, pri tomto ale postupne skonci vsetko)

    minca = mince[index] #vyberieme mincu podla indexu, zaciname s 0 a postupne sa posuvame dalej
    pocet_max = zvysok//minca #maximalne mnozstvo aktualnej mince, ktoru mozeme pouzit, vieme kolko je moznosti s aktualnou mincou na zaciatku

    for i in range(pocet_max, -1, -1): #od max. poctu po index -1(posledny index) po -1(odcitavame, i sa zmensuje -> najprv pouzivame vacsie pocty minci, postupne znizujeme pocet aktualnej najvacsej moznej mince)
        zvysok_novy = zvysok - i * minca #zvysok po pouziti i najvacsej moznej (aktualnej) mince -> stary zvysok - suma zaplatena i mincami (stale tie najvacsie aktualne)
        output_novy = output + [minca] * i #do vyslednej moznosti pridame i aktualnych minci, pretoze tolko sme ich pouzili
        mincovka(index+1, zvysok_novy, output_novy) #rekurzia -> pocitame znova, ale najvacsia minca uz pola pouzita, takze posuvame index o jednu dalej a pracujeme s novym zvyskom a vysledkom, kedze cast sumy uz je zaplatena

mincovka(0, suma, []) #zaciatok, prve volanie, index je 0(prva - najvacsia minca), zvysok je suma(zatial vsetko co treba zaplatit, neskor sa znizuje v rekurzii) a output je prazdny list(postupne tam budeme pridavat mince ako budeme hladat dalsie moznosti)


"""
cele to funguje iba na tom, ze vo for cykle si urcime nove premenne s novymi hodnotami po vyskusani moznosti zaplatenia,
teda sa nam neprepisuju stare a ked nejaka z funkcii vramci rekurzie skonci a vratime sa naspat do napr. prvej, stale tam mame povodny zvysok aj output,
pretoze su to lokalne premenne vramci kazdej z funkcii spustenych v rekurzii

urcite to zvladnes <3 <3
"""

