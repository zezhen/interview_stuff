import collections

def bfs(capacity, edges, resNet, s, t):
    queue = collections.deque([(s, float('inf'), {})])
    while queue:
        node, flow, path = queue.popleft()
        if node == t:
            return flow, path
        for neighbor in edges[node]:
            if neighbor in path: continue
            newpath = path.copy()
            f = capacity[node][neighbor] - resNet[node][neighbor]
            if f > 0:
                newpath[neighbor] = node
                queue.append((neighbor, min(flow, f), newpath))
    return 0, {}

def EdmondsKarp(capacity, s, t):
    maxFlow = 0
    resNet = [[0]*len(capacity) for _ in xrange(len(capacity))]

    edges = collections.defaultdict(list)
    for i, row in enumerate(capacity):
        for j, cap in enumerate(row):
            if cap > 0: edges[i].append(j)

    while True:
        pathFlow, path = bfs(capacity, edges, resNet, s, t)
        # print pathFlow, path, resNet
        if pathFlow == 0: break
        
        maxFlow += pathFlow
        cur = t
        while cur != s:
            prev = path[cur]
            resNet[prev][cur] += pathFlow
            resNet[cur][prev] -= pathFlow
            cur = prev

    return maxFlow


capacity = [[0, 1000000, 1000000, 0], [0, 0, 1, 1000000], [0, 0, 0, 1000000], [0, 0, 0, 0]]
print EdmondsKarp(capacity, 0, 3) == 2000000