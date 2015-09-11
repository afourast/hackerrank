#  import defaultdict as dd
import bisect as bs

def update_blocks(blocks, new_l, new_r, c, d):
    #  blocks = []
    i_l = bs.bisect_right(blocks, [new_l])
    i_r = bs.bisect_right(blocks, [new_r])
    print i_l, i_r
    for i in xrange(i_l, i_r):
        blocks[i][1] += c
        blocks[i][2] += d
    if blocks[i_l - 1][0] == new_l:
        blocks[i_l - 1][1] += c
        blocks[i_l - 1][2] += d
        if blocks[i_r - 1][0] == new_r:
            return
        else:
            blocks.insert(i_r, [new_r, blocks[i_r - 1][1]-c, blocks[i_r - 1][2]-d])
    else:
        blocks.insert(i_l, [new_l, blocks[i_l - 1][1]+c, blocks[i_l - 1][2]+d])
        if blocks[i_r][0] == new_r:
            return
        else:
            blocks.insert(i_r+1, [new_r, blocks[i_r][1]-c, blocks[i_r][2]-d])

def q1(blocks, new_l, new_r, c):
    update_blocks(blocks, new_l, new_r, c, 0)

def q2(blocks, new_l, new_r, d):
    update_blocks(blocks, new_l, new_r, 0, d)

def q3(blocks, l, r):
    pass


