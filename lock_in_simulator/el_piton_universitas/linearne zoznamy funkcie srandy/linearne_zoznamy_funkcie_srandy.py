
class Prvek:
    def __init__(self, h, d=None):
        self.hodnota = h
        self.dalsi = d


class LSS:
    def __init__(self):
        self.zac = None

    def PridejHodnotuNaZacatek(self, h):
        self.zac = Prvek(h, self.zac)

    def OtocSeznam(self):
        prvky = []
        pom = self.zac
        while pom:
            prvky.append(pom)
            pom = pom.dalsi

        prvky.reverse()

        if not prvky:
            self.zac = None
            return

        self.zac = prvky[0]
        for i in range(len(prvky)-1):
            prvky[i].dalsi = prvky[i+1]
        prvky[-1].dalsi = None
        return

    def VypustPrvek(self, p): 
        if p is None:
            return

        prvky = []
        pom = self.zac
        while pom is not None:
            prvky.append(pom)
            pom = pom.dalsi

        prvky.pop(p)

        if not prvky:
            self.zac = None
            return

        self.zac = prvky[0]
        for i in range(len(prvky) - 1):
            prvky[i].dalsi = prvky[i+1]
        prvky[-1].dalsi = None
        return


    def VypustPrvkySHodnotou(self, h):
        prvky = []
        pom = self.zac
        while pom:
            if pom.hodnota != h:
                prvky.append(pom)
            pom = pom.dalsi

        if not prvky:
            self.zac = None
            return

        self.zac = prvky[0]
        for i in range(len(prvky) - 1):
            prvky[i].dalsi = prvky[i+1]
        prvky[-1].dalsi = None
        return

    def VypustPrvkySHodnotouVetsiNez(self, h):
        prvky = []
        pom = self.zac
        while pom:
            if pom.hodnota <= h:
                prvky.append(pom)
            pom = pom.dalsi

        if not prvky:
            self.zac = None
            return

        self.zac = prvky[0]
        for i in range(len(prvky) - 1):
            prvky[i].dalsi = prvky[i+1]
        prvky[-1].dalsi = None
        return

    def NajdiPrvekSHodnotou(self, h):
        pom = self.zac
        i = 0
        while pom is not None:
            if pom.hodnota == h:
                return i
            pom = pom.dalsi
            i += 1
        return None
     

    def NajdiPrvekSHodnotouVetsiNez(self, h):
        prvky = []
        prvkysorted = []
        pom = self.zac
        najmensi = None

        while pom:
            prvky.append(pom.hodnota)
            pom = pom.dalsi
        
        prvkysorted = prvky[:]
        prvkysorted.sort()

        for i in range(len(prvky)):
            if prvkysorted[i] > h:
                return prvky.index(prvkysorted[i])
        return None
            
    def Vypis(self):
        """vypise hodnoty ze sezanmu na jeden radek"""
        pom = self.zac
        while pom is not None:
            print(pom.hodnota, end=' ')
            pom = pom.dalsi
        print('')       # konec radku

s = LSS()
pocet_prikazu = int(input())
for _ in range(pocet_prikazu):
    radek = input().split()
    prikaz = radek[0]
    parametry = radek[1:]
    if prikaz == 'OtocSeznam':
        s.OtocSeznam()
    elif prikaz == 'PridejHodnotuNaZacatek':
            s.PridejHodnotuNaZacatek(int(parametry[0]))
    elif prikaz == 'VypustPrvek':
        if parametry[0] == '=':
            p = s.NajdiPrvekSHodnotou(int(parametry[1]))
            s.VypustPrvek(p)
        elif parametry[0] == '>':
            p = s.NajdiPrvekSHodnotouVetsiNez(int(parametry[1]))
            s.VypustPrvek(p)
        else:
            print(f'Neznamy parametr v prikazu "{prikaz} {parametry[0]}"')
    elif prikaz == 'VypustPrvkySHodnotou':
        s.VypustPrvkySHodnotou(int(parametry[0]))
    elif prikaz == 'VypustPrvkySHodnotouVetsiNez':
        s.VypustPrvkySHodnotouVetsiNez(int(parametry[0]))
    else:
        print(f'Neznamy prikaz "{prikaz}"',)
    s.Vypis()


