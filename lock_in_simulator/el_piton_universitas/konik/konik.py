m, n, sx, sy = map(int, input().strip().split())
sx -= 1
sy -= 1

moznosti = [(-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1)]

prejdene = []
for _ in range(n):
    riadok = [False]*m
    prejdene.append(riadok)

tahov_spolu = m*n
hotovo = False

def jazdec(x, y, tahy):
    global hotovo

    if hotovo:
        return

    if tahy == tahov_spolu:
        hotovo = True
        return
    
    for tah_x, tah_y in moznosti:
        pos_x = x + tah_x
        pos_y = y + tah_y

        if 0 <= pos_x < m and 0 <= pos_y < n:
            if not prejdene[pos_y][pos_x]:
                prejdene[pos_y][pos_x] = True
                jazdec(pos_x, pos_y, tahy+1)
                prejdene[pos_y][pos_x] = False

prejdene[sy][sx] = True
jazdec(sx, sy, 1)

if hotovo:
    print("ANO")
else:
    print("NE")