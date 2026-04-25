class Prvek:

    def __init__(self, h, popis):
        self.hodnota = h
        self.popis = popis
        self.dalsi = None     #  tady si prvek pamatuje naslednika

class SetridenySeznam:
 
    def __init__(self):
        # seznam ma odkaz na prvni prvek seznamu, ktery ma minimalni hodnotu v seznamu
        self.zac = None

 
    def vloz(self, h, popis):
        """Vlozi do seznamu novy prvek s hodnotou h.
        Kdyz tam uz prvek s hodnotou h je v seznamu, tak prida dalsi kopii.
        """
        novy = Prvek(h, popis)
        if self.zac is None or h < self.zac.hodnota:
            novy.dalsi = self.zac
            self.zac = novy
            return

        pom = self.zac
        while pom.dalsi and pom.dalsi.hodnota <= h:
            pom = pom.dalsi

        novy.dalsi = pom.dalsi
        pom.dalsi = novy
        
        pass        


    def vypis(self):
        """vypise prvky seznamu na jeden radek"""
        pom = self.zac
        while pom:
            print('(', str(pom.hodnota), ',', pom.popis, ')',sep='', end=' ')
            pom = pom.dalsi
        print('')       # konec radku

def slejDestruktivne(s1, s2):
    '''Slej dva setridene seznamy s1 a s2 do jednoho setrideneho seznamu novy.
    Nebudou se vytvaret zadne nove prvky ani jine datove struktury. Seznamy
    s1 a s2 budou touto operaci zniceny a na konci zustanou prazdne!
    '''
    novy = SetridenySeznam()

    # TADY PRIJDE VAS KOD
    p1 = s1.zac
    p2 = s2.zac
    koniec = None

    while p1 and p2:
        if p1.hodnota <= p2.hodnota:
            vybrany = p1
            p1 = p1.dalsi
        else:
            vybrany = p2
            p2 = p2.dalsi

        vybrany.dalsi = None

        if novy.zac is None:
            novy.zac = vybrany
            koniec = vybrany
        else:
            koniec.dalsi = vybrany
            koniec = vybrany

    zvysok = p1 if p1 else p2
    if zvysok:
        if novy.zac is None:
            novy.zac = zvysok
        else:
            koniec.dalsi = zvysok
    # nasledujici radky musi zustat na konci funkce, aby se zarucilo, ze
    # seznamy s1 a s2 zustanou prazdne.
    s1.zac = None   
    s2.zac = None
    return novy

delka1, delka2 = [int(i) for i in input().split()]

seznam1 = SetridenySeznam()
for i in range(delka1):
    line = input().split()
    seznam1.vloz(int(line[0]), line[1])
seznam1.vypis()

seznam2 = SetridenySeznam()
for i in range(delka2):
    line = input().split()
    seznam2.vloz(int(line[0]), line[1])
seznam2.vypis()

novy = slejDestruktivne(seznam1, seznam2)
novy.vypis()
                
