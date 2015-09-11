def solve():
    pr.sort(reverse=True)
    return pr[0] + pr[2] + pr[4]

pr = []
for i in range(10):
    pr.append(int(raw_input()))
sol = solve()
print "%d"%(sol)

