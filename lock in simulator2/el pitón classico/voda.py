from collections import deque

vstup = list(map(int, input().strip().split()))

def voda(kapacita, objem):
    a, b, c = kapacita
    zaciatok = tuple(objem)

    fronta = deque([(zaciatok, 0)])
    naliate = {zaciatok: 0}
    vysledok = {}

    while fronta:
        aktualny, pocet_preliati = fronta.popleft()

        for i in aktualny:
            if i not in vysledok or pocet_preliati < vysledok[i]:
                vysledok[i] = pocet_preliati

        for i in range(3):
            for j in range(3):
                if i==j:
                    continue

                novy = list(aktualny)
                mnozstvo = min(aktualny[i], objem[j]-aktualny[j])

                if mnozstvo > 0:
                    novy[i] -= mnozstvo
                    novy[j] += mnozstvo

                    stav = tuple(novy)

                    if stav not in naliate:
                        naliate[stav] = pocet_preliati + 1
                        fronta.append((stav, pocet_preliati + 1))

    for k in sorted(vysledok.keys()):
        print(f"{k}:{vysledok[k]}")

    #output = [f"{k}:{vysledok[k]}" for k in sorted(vysledok.keys())]
    #print(" ".join(output))


def solve(capacities, initial):
    max_a, max_b, max_c = capacities
    start_state = tuple(initial)
    
    # queue: (stav, pocet_preliti)
    queue = deque([(start_state, 0)])
    visited = {start_state: 0}
    results = {}

    while queue:
        curr, dist = queue.popleft()
        
        # Zaznamenání dosažených objemů
        for amount in curr:
            if amount not in results or dist < results[amount]:
                results[amount] = dist
        
        # Všechny dvojice (odkud, kam)
        for i in range(3):
            for j in range(3):
                if i == j: continue
                
                # Logika přelití
                new_state = list(curr)
                amount_to_pour = min(curr[i], capacities[j] - curr[j])
                if amount_to_pour > 0:
                    new_state[i] -= amount_to_pour
                    new_state[j] += amount_to_pour
                    st = tuple(new_state)
                    
                    if st not in visited:
                        visited[st] = dist + 1
                        queue.append((st, dist + 1))

    # Formátování výstupu
    output = [f"{k}:{results[k]}" for k in sorted(results.keys())]
    print(" ".join(output))

vstup = list(map(int, input().strip().split()))
solve((vstup[0], vstup[1], vstup[2]), (vstup[3], vstup[4], vstup[5]))
# Vstup z příkladu: a=4, b=1, c=1 | x=1, y=1, z=1
#solve((4, 1, 1), (1, 1, 1))