#  import defaultdict as dd
import bisect as bs

def update_blocks(blocks, new_l, new_r, c, d):
    i_l = bs.bisect_right(blocks, [new_l])
    i_r = bs.bisect_right(blocks, [new_r])
    for i in xrange(i_l, i_r):
        blocks[i][1] += c%md
        blocks[i][2] += d%md
    if blocks[i_l][0] == new_l:
        if blocks[i_r][0] != new_r:
            blocks.insert(i_r, [new_r, blocks[i_r - 1][1]-c, blocks[i_r - 1][2]-d])
    else:
        blocks.insert(i_l, [new_l, blocks[i_l - 1][1]+c, blocks[i_l - 1][2]+d])
        if blocks[i_r+1][0] != new_r:
            blocks.insert(i_r+1, [new_r, blocks[i_r][1]-c, blocks[i_r][2]-d])

def q1(blocks, new_l, new_r, c):
    update_blocks(blocks, new_l, new_r+1, c, 0)

def q2(blocks, new_l, new_r, d):
    update_blocks(blocks, new_l, new_r+1, 0, d)

def q3(blocks, new_l, new_r):
    new_r += 1
    i_l = bs.bisect_right(blocks, [new_l])
    i_r = bs.bisect_right(blocks, [new_r])
    summ = 0
    for i in xrange(i_l, i_r):
        summ += (blocks[i][1] * blocks[i][2] * (blocks[i+1][0]-blocks[i][0]))%md
    if blocks[i_l][0] != new_l:
        summ += (blocks[i_l-1][1] * blocks[i_l-1][2] * (blocks[i_l][0]-new_l))%md
    if blocks[i_r][0] != new_r:
        summ = (summ+md-blocks[i_r-1][1] * blocks[i_r-1][2] * (blocks[i_r][0]-new_r))%md
    print summ%md

md = 1000000007

n,q = map(int,raw_input().split())
aa = [[0,0,0], [n, 0, 0]]
for i in xrange(q):
    qq = map(int, raw_input().split())
    if qq[0] == 1:
        q1(aa, qq[1]-1, qq[2]-1, qq[3])
    if qq[0] == 2:
        q2(aa, qq[1]-1, qq[2]-1, qq[3])
    if qq[0] == 3:
        q3(aa, qq[1]-1, qq[2]-1)
