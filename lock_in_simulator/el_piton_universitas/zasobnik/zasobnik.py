class zasobnikpole:
    def __init__(self):
        self.pole = []
    def push(self, x):
        self.pole.append(x)
    def pop(self):
        return self.pole.pop()

class frontapole:
    def __init__(self, kapacita):
        self.pole = [None]*kapacita
        self.kapacita = kapacita
        self.zacatek, self.pocet = 0, 0

    def enqueue(self, vkladany):
        if self.pocet == self.kapacita:
            raise IndexError("preplnená fronta")

        self.pole[(self.zacatek+self.pocet)%self.kapacita] = vkladany
        self.pocet += 1

    def dequeue(self):
        if self.pocet == 0:
            raise IndexError("prázdna fronta")
        self.pocet -= 1
        odebirany = self.pole[self.zacatek]
        self.zacatek = (self.zacatek + 1)%self.kapacita
        return odebirany

class uzel:
    def __init__(self, hodnota = None, dalsi = None):
        self.hodnota = hodnota
        self.dalsi = dalsi

class zasobnik:
    def __init__(self):
        self.zacatek = None
    def push(self, hodnota):
        self.zacatek = uzel(hodnota, self.zacatek)
    def pop(self):
        hodnota = self.zacatek.hodnota
        self.zacatek = self.zacatek.dalsi
        return hodnota

class frontaspojovyzeznam:
    def __init__(self):
        self.konec = None
        self.delka = 0
    def dequeue(self):
        odebirany = self.konec.dalsi
        if self.delka == 1:
            self.konec = None
        else:
            self.konec.dalsi = odebirany.dalsi











