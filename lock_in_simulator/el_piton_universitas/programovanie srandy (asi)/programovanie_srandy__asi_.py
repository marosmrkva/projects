class vagon:
    def __init__(self, hod, next):
        self.hod = hod
        self.next = next


class spojak:
    def init(self):
        self.zac = None
        self.kon = None

    def pridej_na_zacatek(self, co):
        self.zac = vagon(co, self.zac)
        if(self.kon == None): self.kon = self.zac

    def pridej_na_konec(self, co):
        if(self.kon == None):
            self.pridej_na_zacatek(co)
        else:
            pom = vagon(co, None)
            self.kon.next = pom
            self.kon = self.kon.next


    def uber(self):
        pom = self.zac.hod
        self.zac = self.zac.next
        

        return pom




s = spojak()
s.pridej_na_konec(1)
s.pridej_na_konec(2)
s.pridej_na_konec(3)
s.pridej_na_konec(4)
s.pridej_na_konec(5)

print("chuj w dupe")







