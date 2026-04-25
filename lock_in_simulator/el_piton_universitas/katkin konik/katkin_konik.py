
m, n, sx, sy = map(int, input().split()) #vsup, indexovani od 1
# x = sloupec, y = radek, indexovani od 0
sx -= 1
sy -= 1

# vsechny mozne tahy jezdce
moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

# visited[y][x] = True => uz jsme policko navstivili
visited = []
for _ in range(n):
    radek = [False] * m
    visited.append(radek) # tabulka z False

# pocet poli
total_cells = m * n

# promenna do ktere si ulozime jestli jsme nasli cestu
found = False

# rekurzivni funkce ktera zkousi vsechny mozne cesty (pozice jezdce, kolik poli navstiveno)
def dfs(x, y, steps):
    global found

    # najde reseni => konec
    if found:
        return

    # vsechna pole prave jednou
    if steps == total_cells:
        found = True
        return

    # zkusime vsechny tahy jezdce
    for dx, dy in moves:
        nx = x + dx #sloupek
        ny = y + dy #radek

        # Kontrola, ze jsme porad na sachovnici
        if 0 <= nx < m and 0 <= ny < n:
            if not visited[ny][nx]: # na tom poli jsme jeste nebyl
                
                visited[ny][nx] = True # oznacime navstivene

                dfs(nx, ny, steps + 1) # dal rekurzi
                visited[ny][nx] = False # vratime stav tabulky

visited[sy][sx] = True #startovni => navstivene

dfs(sx, sy, 1)

if found:
    print("ANO")
else:
    print("NE")