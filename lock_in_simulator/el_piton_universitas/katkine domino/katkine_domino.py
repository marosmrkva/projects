def main():
    N, Z = map(int, input().split()) #pocet kostek, pocatecni hodnota

    # druhy radek
    raw = input().split()
    nums = []

    # rozdeluje na cifry
    for x in raw:
        for c in x:
            nums.append(int(c))
    
    # tabulka 7*7, kolik dvojic mame
    count = [[0] * 7 for i in range(7)]

    for i in range(0, 2 * N, 2):
        a = nums[i]
        b = nums[i + 1]
        x = min(a, b)
        y = max(a, b)
        count[x][y] += 1
    # jen horni trojuhelnik tabulky

    # --- 3) HLEDANI NEJDELSI RADY (DFS + backtracking) ---

    best_len = 0         # nejlepsi delka
    best_path = []       # nejlepsi rada, seznam dvojic
    path = []            # aktualni rada

    def dfs(cur, length): # cur=aktualni cislo na konci rady, length=kolik kostek v aktualni rade
 
        nonlocal best_len, best_path # v main

        # aktualizace nejlepsi rady
        if length > best_len:
            best_len = length
            best_path = path[:]  # kopie

        # z cur do dalsiho cisla (0-6)
        for nxt in range(7):
            x = min(cur, nxt)
            y = max(cur, nxt)

            if count[x][y] > 0:
                # mame k dispozici kostku
                count[x][y] -= 1         
                path.append((cur, nxt))  # pridame s orientaci

                dfs(nxt, length + 1)     # jdeme dal

                # backtracking (odebereme z rady, vratime do tabulky)
                path.pop()
                count[x][y] += 1

    dfs(Z, 0)

    # vysledek
    print(best_len)

    if best_len == 0:
        print()
    else:
        # spravne zapsany vysledek
        out = []
        for (a, b) in best_path:
            out.append(str(a) + str(b))

        print(" ".join(out))

main()

