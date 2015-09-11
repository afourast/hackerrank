#  import defaultdict as dd
import bisect as bs

def update_blocks(blocks, new_l, new_r, c, d):
    #  blocks = []
    i_l = bs.bisect_right(blocks, [new_l])
    i_r = bs.bisect_right(blocks, [new_r])
    for i in xrange(i_l, i_r):
        blocks[i][1] += c
        blocks[i][2] += d
    if blocks[i_l][0] == new_l:
        if blocks[i_r][0] != new_r:
            blocks.insert(i_r, [new_r, blocks[i_r - 1][1]-c, blocks[i_r - 1][2]-d])
    else:
        blocks.insert(i_l, [new_l, blocks[i_l - 1][1]+c, blocks[i_l - 1][2]+d])
        if blocks[i_r+1][0] != new_r:
            blocks.insert(i_r+1, [new_r, blocks[i_r][1]-c, blocks[i_r][2]-d])

def q1(blocks, new_l, new_r, c):
    update_blocks(blocks, new_l, new_r, c, 0)

def q2(blocks, new_l, new_r, d):
    update_blocks(blocks, new_l, new_r, 0, d)

def q3(blocks, new_l, new_r):
    i_l = bs.bisect_right(blocks, [new_l])
    i_r = bs.bisect_right(blocks, [new_r])
    summ = 0
    for i in xrange(i_l, i_r):
        summ += blocks[i][1] * blocks[i][2] * (blocks[i+1][0]-blocks[i][0])
    if blocks[i_l][0] == new_l:
        if blocks[i_r][0] != new_r:
            blocks.insert(i_r, [new_r, blocks[i_r - 1][1]-c, blocks[i_r - 1][2]-d])
    else:
        blocks.insert(i_l, [new_l, blocks[i_l - 1][1]+c, blocks[i_l - 1][2]+d])
        if blocks[i_r+1][0] != new_r:
            blocks.insert(i_r+1, [new_r, blocks[i_r][1]-c, blocks[i_r][2]-d])
    print summ
    


a = [[0, 2, 0], [10, 3, 0], [25, 0, 0], [80, 4, 0]]
b = [[0, 2, 0], [10, 3, 0], [25, 0, 0], [80, 4, 0]]

#  q2(b,10,50,2)
print a
q2(a,20,50,2)
print a
print
print b
q2(b,10,80,2)
print b



