
import random
from itertools import product


def generate_paints(age):
    def create_paint(ii, jj, relation):
        def inner_paint(i, j, N, M):
            if 0 <= i+ii[0] < N and -1 <= i+ii[1] <= N and 0 <= j+jj[0] < M and -1 <= j+jj[1] <= M:
                for r in xrange(*ii):
                    for c in xrange(*jj):
                        if relation(r, c):
                            yield i+r, j+c
        return inner_paint

    return [
        create_paint(ii, jj, relation)
        for ii, jj, relation in product(
            [(0, age), (0, -age, -1)],
            [(0, age), (0, -age, -1)],
            [lambda r, c: abs(r)>=abs(c), lambda r, c: abs(r)<=abs(c), lambda r, c: age-abs(c)-1 >= abs(r)]
        )
    ]

def paint(paints, grid, i, j, N, M):
    random.shuffle(paints)

    for p in paints:
        positions = set(p(i, j, N, M))
        if positions and all(grid[r][c] == "#" for r, c in positions):
            return positions
    return set()


def can_be_old(age, grid, N, M):
    paints = generate_paints(age)
    painted = set()
    stepped_on = set(((r, c) for r in xrange(N) for c in xrange(M) if grid[r][c] == "#"))
    for r, c in stepped_on:
        if grid[r][c] == "#" and (r, c) not in painted:
            painted |= paint(paints, grid, r, c, N, M)
    return not (stepped_on - painted)


def solve(N, M, grid):
    a, b = 1, min(N, M)
    while b-a > 1:
        age = (a+b) // 2

        if can_be_old(age, grid, N, M):
            a = age
        else:
            b = age

    if can_be_old(b, grid, N, M):
        return b
    else:
        return a


import sys
N, M = map(int, raw_input().strip().split())
grid = [[c for c in l.strip()] for l in sys.stdin]
print solve(N, M, grid)
