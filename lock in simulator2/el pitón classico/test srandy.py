from numpy import *

x = 65533
x = ~x
print(x, format(x, "04X"))

x = 65533
x = ~x
x = uint16(x)
print(x, format(x, "04X"))