class VrcholBinStromu:
    """třída pro reprezentaci vrcholu binárního stromu""" 
    def __init__(self, data = None, levy = None, pravy = None):
        self.data = data      # číslo uložené ve vrcholu (nemělo by se měnit)
        self.levy = levy   # levé dítě 
        self.pravy = pravy # pravé dítě

def cena(koren: VrcholBinStromu) -> int:
    """
    koren : kořen zadaného binárního stromu
    vrátí : cenu zadaného stromu

    """

    if koren == None:
        return None
    
    def hladaj(uzol, hlbka):
        hodnota = 0
        a=0
        b=0

        if uzol.levy == None or uzol.pravy == None:
            hodnota = uzol.data * hlbka
            return hodnota
        if uzol.levy:
            a += hladaj(uzol.levy, hlbka+1)
        if uzol.pravy:
            b += hladaj(uzol.pravy, hlbka+1)
        
        return a+b

    return(hladaj(koren, 0))


strom = VrcholBinStromu(None, VrcholBinStromu(None, VrcholBinStromu(40), VrcholBinStromu(None, VrcholBinStromu(10), VrcholBinStromu(5))), VrcholBinStromu(None, VrcholBinStromu(20), VrcholBinStromu(20)))

print(cena(strom))