class VrcholBinStromu:
    """třída pro reprezentaci vrcholu binárního stromu""" 
    def __init__(self, data = None, levy = None, pravy = None):
        self.data = data      # číslo uložené ve vrcholu (nemělo by se měnit)
        self.levy = levy   # levé dítě 
        self.pravy = pravy # pravé dítě


def cena(koren: VrcholBinStromu) -> int:
    def rekurzia(vrchol: VrcholBinStromu, hlbka):
        if not vrchol.levy and not vrchol.pravy:
            return vrchol.data*hlbka
        
        a = 0
        b = 0
        if vrchol.levy:
            a = rekurzia(vrchol.levy, hlbka+1)
        if vrchol.pravy:
            b = rekurzia(vrchol.pravy, hlbka+1)

        return a+b
    
    return rekurzia(koren, 0)
        


vstup = VrcholBinStromu("", VrcholBinStromu("", VrcholBinStromu(40), VrcholBinStromu("", VrcholBinStromu(10), VrcholBinStromu(5))), VrcholBinStromu("", VrcholBinStromu(20), VrcholBinStromu(20)))


print(cena(vstup))