
def neighbors(N, M, r, c):
    c1 = c<M-1
    c2 = r<N-1
    if c1:
        yield r*M + c+1
    if c1 and c2:
        yield (r+1)*M + c+1
    if c2:
        yield (r+1)*M + c


def checks(this, right, diag, bottom):
    yield [this, right, bottom]
    yield [this, right, diag]
    yield [right, diag, bottom]
    yield [this, bottom, diag]


def solve(N, M, grid):
    grids = [
        [
            [1]*4 if grid[i][j] == "#" else [0]*4
            for i in xrange(N) for j in xrange(M)
        ]
        for k in xrange(2)
    ]
    read, write = 0, 1

    count = sum(
        1 for i in xrange(N)
        for j in xrange(M)
        if grid[i][j] == "#"
    )

    for size in xrange(1, min(N, M)):
        #print grids[read][:(N-size+1)*(M-size+1)]
        NN = N-size+1
        MM = M-size+1
        #print NN, MM

        #for r in xrange(N):
        #    for c in xrange(M):
        #        grids[write][r*M + c] = [0]*4

        new_count = 0
        points = set()
        for r in xrange(NN-1):
            for c in xrange(MM-1):
                this_read = r*MM + c
                this_write = r*(MM-1) + c

                params = [this_read] + list(neighbors(NN, MM, r, c))
                for i, idxs in enumerate(checks(*params)):
                    print i, [grids[read][idx][i] for idx in idxs], idxs
                    if all(
                        grids[read][idx][i] == 1 for idx in idxs
                    ):
                        grids[write][this_write][i] = 1
                        points.update(idxs)
                    else:
                        grids[write][this_write][i] = 0

                new_count += int(any(grids[write][this_write]))
                print points

                print grids[write][:(NN-1)*(MM-1)]
                print

        if len(points) != count:
            return size
        else:
            count = new_count

        read, write = write, read
    return min(N, M)


import sys
N, M = map(int, raw_input().strip().split())
grid = [[c for c in l.strip()] for l in sys.stdin]
print solve(N, M, grid)
