translate = dict()
translate['*'] = "1"
translate['.'] = "0"

solutions = dict()

def place(m, row_idx, grid, diags, mask):
    if (row_idx, diags) in solutions.keys():
        return solutions[row_idx, diags]
    ways = 0
    row = grid[row_idx]
    avail = diags[0] | diags[1] | row
    for c in xrange(m):
        if avail & (1<<c):
            continue
        if len(grid) - row_idx > 1:
            inv_row = (~row) & mask
            newdiags = (diags[0] & inv_row, diags[1] & inv_row)
            newdiags = (newdiags[0] | (1<<c), newdiags[1] | (1<<c))
            newdiags = ((newdiags[0]>>1) & mask, (newdiags[1]<<1) & mask)
            ways += place(M, row_idx + 1, grid, newdiags, mask)
        else:
            ways += 1
    solutions[row_idx, diags] = ways
    return ways

def solve(n, m, grid):
    mask = int("1"*m, 2)
    diags = (0, 0)
    return place(m, 0, grid, diags, mask)

import sys
N, M = map(int, raw_input().strip().split())
grid = [int("".join(map(lambda x: translate[x], [c for c in l.strip()])), 2) for l in sys.stdin]
print solve(N, M, grid)
