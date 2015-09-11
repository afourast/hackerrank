
def walk(bridges, bridge):
    start = bridge
    current = bridge
    seen = set()
    seen.add(current)
    while True:
        next = bridges[current]
        if next in seen:
            return seen, (start, current)
        seen.add(next)
        current = next

def solve(bridges):
    cities = set(range(1, len(bridges)+1))

    walks = 0
    while cities:
        start = next(iter(cities))
        visited, _ = walk(bridges, start)
        cities -= visited
        walks += 1

    return walks - 1

T = int(raw_input())
for t in xrange(1, T+1):
    N = int(raw_input())
    bridges = dict(zip(range(1, N+1), map(int, raw_input().strip().split())))

    print solve(bridges)

