import sys

def solve():
    try:
        input_data = sys.stdin.read().split()
        if not input_data:
            return
        
        n = int(input_data[0])
        m = int(input_data[1])
        
        adj = [[] for _ in range(n + 1)]
        idx = 2
        for _ in range(m):
            u = int(input_data[idx])
            v = int(input_data[idx+1])
            adj[u].append(v)
            adj[v].append(u)
            idx += 2
    except EOFError:
        return

    colors = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if colors[i] == 0:
            stack = [(i, 1)]
            colors[i] = 1
            
            while stack:
                u, c = stack.pop()
                next_color = 2 if c == 1 else 1
                
                for v in adj[u]:
                    if colors[v] == 0:
                        colors[v] = next_color
                        stack.append((v, next_color))
                    elif colors[v] == c:
                        print("Nelze")
                        return

    group1 = [str(i) for i in range(1, n + 1) if colors[i] == 1]
    group2 = [str(i) for i in range(1, n + 1) if colors[i] == 2]

    print(" ".join(group1))
    print(" ".join(group2))

if __name__ == "__main__":
    solve()
