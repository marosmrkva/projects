from numpy import uint8, uint16

cislo = 127
cislo = ~cislo
print(cislo, format(cislo, "02X"))
"""
cislo = 127
cislo = ~cislo
cislo = uint8(cislo)
print(cislo, format(cislo, "02X"))

cislo = 127
cislo = ~cislo
cislo = uint16(uint8(cislo))
print(cislo, format(cislo, "02X"))
"""
cislo = 127
cislo = ~cislo
cislo = uint16(cislo)
print(cislo, format(cislo, "02X"))
