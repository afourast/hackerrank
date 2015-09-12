
import sys
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


def step_on_it(N, M, grid, size, steps):
    paints = generate_paints(size)
    for i in xrange(steps):
        random.shuffle(paints)
        r, c = random.randint(0, N-1), random.randint(0, M-1)
        for pos in paints[0](r, c, N, M):
            grid[pos[0]][pos[1]] = "#"


size, N, M, steps = map(int, sys.argv[1:])
grid = [["." for c in xrange(M)] for r in xrange(N)]
step_on_it(N, M, grid, size, steps)

print N, M
for g in grid:
    print "".join(g)
