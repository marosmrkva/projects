import numpy as np

cislo = 127

cislo = ~cislo
print(bin(cislo))
cislo = np.uint16(cislo)

print(cislo, format(cislo, "02X"))