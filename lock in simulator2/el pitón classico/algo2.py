a = [2,8,5,8,0,0,7,2,0,20]
b = [10,8,20,0,2,2,10,7]
a.sort()
b.sort()

def najdi(a, b):
    c = []
    pointer_a = 0
    pointer_b = 0

    while pointer_a != len(a)-1 or pointer_b != len(b)-1:
        if a[pointer_a] == b[pointer_b]:
            pocet_a = 0
            pocet_b = 0
            aktualny = a[pointer_a]
            while aktualny == a[pointer_a]:
                pocet_a += 1
                pointer_a += 1
            while aktualny == b[pointer_b]:
                pocet_b += 1
                pointer_b += 1
            
            for _ in range(abs(pocet_a-pocet_b)):
                c.append(aktualny)

        else:
            if a[pointer_a] < b[pointer_b]:
                c.append(a[pointer_a])
                pointer_a += 1
            elif a[pointer_a] > b[pointer_b]:
                c.append(b[pointer_b])
                pointer_b += 1
    print(c)

najdi(a,b)



class VrcholBinStromu:

   """třída pro reprezentaci vrcholu binárního stromu"""  
   def  __init__(self, data =  None, levy =  None, pravy =  None):
      self.levy = levy    # levé dítě  
      self.pravy = pravy  # pravé dítě
      self.data = data    # hodnoty (operátory či operandy) uložené ve vrcholech
  
strom = VrcholBinStromu("or", VrcholBinStromu("not", VrcholBinStromu("and", VrcholBinStromu("or", VrcholBinStromu(True), VrcholBinStromu(False)), VrcholBinStromu("and", VrcholBinStromu(True), VrcholBinStromu(True)))), VrcholBinStromu("or", VrcholBinStromu("and", VrcholBinStromu(False), VrcholBinStromu("or", VrcholBinStromu(False), VrcholBinStromu(True))), VrcholBinStromu("or", VrcholBinStromu(True))))

"""def vyska(koren: VrcholBinStromu, h: bool):

    """
"""
    koren : kořen zadaného binárního stromu
    h     : True či False
    vrátí : maximální výšku podstromu reprezentujícího podvýraz, který se vyhodnotí na hodnotu h
    """
"""

    if koren == None:
        return None
    
    maximum = [None]

    def vyhodnot(uzol):
        if uzol.levy == None and uzol.pravy == None:
            aktualna_hodnota = uzol.data
            aktualna_vyska = 0

            if aktualna_hodnota == h:
                if maximum[0] == None or aktualna_vyska > maximum[0]:
                    maximum[0] = aktualna_vyska
                
            return aktualna_hodnota, aktualna_vyska
        
        if uzol.data == "not":
            lavy_hodnota, lavy_vyska = vyhodnot(uzol.levy)

            aktualna_hodnota = not lavy_hodnota
            aktualna_vyska = lavy_vyska+1

        else:
            lavy_hodnota, lavy_vyska = vyhodnot(uzol.levy)
            pravy_hodnota, pravy_vyska = vyhodnot(uzol.pravy)

            aktualna_vyska = max(lavy_vyska, pravy_vyska)+1

            if uzol.data == "and":
                aktualna_hodnota == lavy_hodnota and pravy_hodnota
            else:
                aktualna_hodnota == lavy_hodnota or pravy_hodnota

            if aktualna_hodnota == h:
                if maximum[0] == None or aktualna_vyska > maximum[0]:
                    maximum[0] = aktualna_vyska

            return aktualna_hodnota, aktualna_vyska
    
    vyhodnot(koren)

    return maximum[0]"""

def vyska(koren: VrcholBinStromu, h: bool):
    """
    koren : kořen zadaného binárního stromu
    h     : hledaná logická hodnota (True nebo False)
    vrátí : maximální výšku podstromu, který se vyhodnotí na h, nebo None
    """
    
    # Pokud je strom prázdný, neexistuje žádný podstrom
    if koren is None:
        return None

    # Použijeme seznam jako "kontejner" pro uložení maximální nalezené výšky.
    # Uvnitř seznamu bude buď None (zatím nic nenalezeno) nebo číslo (výška).
    vysledek = [None] 

    def _projdi(uzel):
        """
        Rekurzivní funkce.
        Vrací dvojici: (logická_hodnota_podstromu, výška_podstromu)
        """
        # 1. Základní případ: List (obsahuje bool hodnotu)
        # Poznámka: v zadání se píše, že listy jsou bool, vnitřní uzly str.
        if isinstance(uzel.data, bool):
            aktualni_hodnota = uzel.data
            aktualni_vyska = 0 # Samotný list má výšku 0
            
            # Kontrola, zda se list shoduje s h
            if aktualni_hodnota == h:
                # Pokud jsme zatím nic nenašli (None) nebo je tato výška větší
                if vysledek[0] is None or aktualni_vyska > vysledek[0]:
                    vysledek[0] = aktualni_vyska
            
            return aktualni_hodnota, aktualni_vyska

        # 2. Rekurzivní krok pro operátory
        # Musíme nejprve vyhodnotit syny, abychom znali jejich hodnoty a výšky
        
        # Operátor NOT má jen levého syna (dle zadání)
        if uzel.data == 'not':
            levy_val, levy_h = _projdi(uzel.levy)
            
            aktualni_hodnota = not levy_val
            aktualni_vyska = levy_h + 1
            
        # Operátory AND / OR mají oba syny
        else: # 'and' nebo 'or'
            levy_val, levy_h = _projdi(uzel.levy)
            pravy_val, pravy_h = _projdi(uzel.pravy)
            
            aktualni_vyska = max(levy_h, pravy_h) + 1
            
            if uzel.data == 'and':
                aktualni_hodnota = levy_val and pravy_val
            else: # 'or'
                aktualni_hodnota = levy_val or pravy_val
        
        # 3. Kontrola aktuálního podstromu vůči hledané hodnotě h
        if aktualni_hodnota == h:
            # Aktualizace globálního maxima
            if vysledek[0] is None or aktualni_vyska > vysledek[0]:
                vysledek[0] = aktualni_vyska
                
        # Vracíme hodnoty nahoru rodiči
        return aktualni_hodnota, aktualni_vyska

    # Spustíme rekurzi
    _projdi(koren)
    
    # Vrátíme obsah kontejneru (buď číslo nebo None)
    return vysledek[0]

print(vyska(strom, True))
        




