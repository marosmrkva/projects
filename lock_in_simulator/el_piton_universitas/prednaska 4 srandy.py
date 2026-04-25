import sys

def f():
    print("nazdar")
f()

a = sys.stdin.read()
b = sys.stdin.readline()
c = sys.stdin.readline()
print()

class student:
    def __init__(self, jmeno, prijmeni, cislo):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.cislo = cislo
        
    def predstavse(self):
        print("dobry den, ja jsem", self.jmeno, self.prijmeni)

class matfyzak(student):
    def premyslej():
        print("premyslim az se ze mne kouri")

s = student.__init__("Peťko", "Kotov", 12345678)
s.predstavse()

m = matfyzak
m.premyslej()


