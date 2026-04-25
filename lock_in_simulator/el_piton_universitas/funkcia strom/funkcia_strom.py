
def strom(x, y, d, les, znak):
    length = 0
    for i in range(d): #kmen
        bod(x, y, znak, les)
        y+=1
        length += 1
        if length == d:
            break
    trojuholnik(5, x, y+d)
    trojuholnik(5, x, y+d+4)
    trojuholnik(4, x, y+d+7)
