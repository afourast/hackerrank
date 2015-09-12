#  import defaultdict as dd
import bisect as bs


def update_blocks(blocks, new_l, new_r, c, d):
    i_l = bs.bisect_right(blocks, [new_l])
    i_r = bs.bisect_right(blocks, [new_r])
    #print blocks, i_r, i_l
    for i in xrange(i_l, i_r):
        blocks[i][1] += c%md
        blocks[i][2] += d%md

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
        summ = summ % md
    if blocks[i_l][0] != new_l:
        summ += (blocks[i_l-1][1] * blocks[i_l-1][2] * (blocks[i_l][0]-new_l))%md
        summ = summ % md
    if blocks[i_r][0] != new_r:
        summ = (summ - blocks[i_r-1][1] * blocks[i_r-1][2] * (blocks[i_r][0]-new_r))%md
    print summ

md = 1000000007

n,q = map(int,raw_input().split())
aa = []
commands = []
lrs = set([0, n])
for i in xrange(q):
    commands.append(map(int, raw_input().split()))
for c in commands:
    if c[0] != 3:
        lrs.add(c[1]-1)
        lrs.add(c[2])
for l in sorted(lrs):
    aa.append([l, 0, 0])
appends = []
for qq in commands:
    if qq[0] != 3:
        appends.append(qq)
    else:
        appends.sort(key=lambda x: x[2]-x[1], reverse=True)
        for qqq in appends:
            if qqq[0] == 1:
                q1(aa, qqq[1]-1, qqq[2]-1, qqq[3])
            if qqq[0] == 2:
                q2(aa, qqq[1]-1, qqq[2]-1, qqq[3])
        appends = []
        q3(aa, qq[1]-1, qq[2]-1)
