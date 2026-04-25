class Prvek:
    def __init__(self, hodnota):
        self.hodnota = hodnota
        self.dalsi = None

def vynech_hodnotu(hlava, h):
    """
    Odstran vsechny vyskyty hodnoty h v seznamu hlava. 
    Vraci hlavu vysledneho seznamu.
    """
    pom = hlava
    predchozi = None

    while pom:
        if pom.hodnota == h:
            if predchozi:
                predchozi.dalsi = pom.dalsi
            else:
                hlava = pom.dalsi
        predchozi = pom
        pom = pom.dalsi

    return hlava

def vypis(hlava):
    p = hlava
    while p:
        print(p.hodnota, end=" ")
        p = p.dalsi
    print("")

hlava = Prvek(1)
vypis(hlava)
hlava.dalsi = Prvek(2)
vypis(hlava)
hlava.dalsi.dalsi = Prvek(3)
vypis(hlava)
hlava.dalsi.dalsi.dalsi = Prvek(4)
vypis(hlava)

nova_hlava = vynech_hodnotu(hlava,2)
