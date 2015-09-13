from collections import defaultdict

def edgescore(edge,edges,nodes,tree,mem):

  if edge in mem:
    return mem[edge]

  to = edge[1]
  fr = edge[0]

  score = 0
  for new_edge in tree[to]:
    if new_edge[1] == fr:
      score += nodes[to-1]
      continue
    edge_sc = edgescore(new_edge,edges,nodes,tree,mem)
    score += edge_sc

  mem[edge] =  score
  return score


def solve(edges,nodes,tree):
  mem = {}
  for e_id,edge in enumerate(edges):
    if edge not in mem:
      sc = edgescore(edge,edges,nodes,tree,mem)
      mem[edge] = sc

  mx = 0
  for node_id in range(n):
    nd = node_id+1
    sc = nodes[node_id]
    edge_scs = sorted([mem[edge] for edge in tree[nd] ])
    assert(sc+sum(edge_scs)) == sum(nodes)
    sc += sum(edge_scs[:-1])
    if mx<sc:
      mx = sc

  return mx

mem = {}
n = int(raw_input())
nodes = map(int,raw_input().split())
edges = []
tree = defaultdict(lambda:[])
for i in range(n-1):
    edge = tuple(map(int,raw_input().split()))
    edges.append(edge)
    edges.append(tuple(reversed(edge)))
    tree[edge[0]].append(edge)
    tree[edge[1]].append(tuple(reversed(edge)))

sol = solve(edges,nodes,tree)
print "%d"%(sol)



