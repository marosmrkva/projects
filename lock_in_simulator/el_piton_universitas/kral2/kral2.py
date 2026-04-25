import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    it = iter(map(int, input_data))

    try:
        num_obstacles = next(it)
        obstacles = set()
        for _ in range(num_obstacles):
            ox, oy = next(it), next(it)
            obstacles.add((ox, oy))
        
        start_pos = (next(it), next(it))
        target_pos = (next(it), next(it))
    except StopIteration:
        return

    queue = deque([(start_pos[0], start_pos[1], [start_pos])])
    visited = set([start_pos])
    visited.update(obstacles)

    while queue:
        x, y, path = queue.popleft()

        if (x, y) == target_pos:
            for px, py in path:
                print(f"{px} {py}")
            return

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0: continue
                
                nx, ny = x + dx, y + dy
                
                if 1 <= nx <= 8 and 1 <= ny <= 8 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, path + [(nx, ny)]))

    print("-1")

if __name__ == "__main__":
    solve()