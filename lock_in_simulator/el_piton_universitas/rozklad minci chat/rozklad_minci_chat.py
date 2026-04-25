def solve():
    n = int(input().strip())
    coins = list(map(int, input().strip().split()))
    target = int(input().strip())

    result = []

    def backtrack(index, remaining, current):
        if remaining == 0:
            result.append(current.copy())
            return
        if index == n:
            return

        coin = coins[index]
        max_count = remaining // coin

        for count in range(max_count, -1, -1):
            new_remaining = remaining - count * coin
            new_current = current + [coin] * count
            backtrack(index + 1, new_remaining, new_current)

    backtrack(0, target, [])

    for combination in result:
        print(*combination)

solve()
