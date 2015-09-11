
def create_row_mask(M, row, mask):
    row_mask = mask
    for c, v in enumerate(row):
        if v == "*":
            row_mask &= ~(1<<c)
    return row_mask


all_ = []
current = []

def place(M, row_idx, grid, diags, mask):
    ways = 0
    row = grid[row_idx]
    row_mask = create_row_mask(M, row, mask)
    for c in xrange(M):
        if row[c] == "*":
            continue

        newdiags = ((diags[0]>>1) & mask, (diags[1]<<1) & mask)
        if newdiags[0] & (1<<c) or newdiags[1] & (1<<c):
            continue

        # current.append((row_idx, c))

        if len(grid)-row_idx > 1:
            #newdiags = (newdiags[0] & ~(1), newdiags[1] & (1<<M))
            newdiags = (newdiags[0] & row_mask, newdiags[1] & row_mask)
            newdiags = (newdiags[0] | (1<<c), newdiags[1] | (1<<c))
            ways += place(M, row_idx+1, grid, newdiags, mask)
        else:
            ways += 1
            # all_.append(current[:])
            # current.pop()

    return ways


def solve(N, M, grid):
    mask = int("1"*M, 2)
    diags = (0, 0)
    return place(M, 0, grid, diags, mask)

import sys
N, M = map(int, raw_input().strip().split())
grid = [[c for c in l.strip()] for l in sys.stdin]
print solve(N, M, grid)

# for positioning in all_:
#     for p in positioning:
#         print p
#     print
