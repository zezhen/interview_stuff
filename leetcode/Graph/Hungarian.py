import collections
def preprocess(edges):
    node = collections.defaultdict(set)
    for v1, v2 in edges:
        node[v1].add(v2)
        node[v2].add(v1)
    return node

def hungarian_dfs(edges):
    node = preprocess(edges)

    n = len(node)
    matching = [-1] * n

    def dfs(x, visited):
        for neighbor in node[x]:
            if neighbor in visited: continue
            visited.add(neighbor)
            if matching[neighbor] == -1 or dfs(matching[neighbor], visited):
                # not a match point
                matching[x] = neighbor
                matching[neighbor] = x
                return True
        return False

    ans = 0
    for i in xrange(n):
        if matching[i] != -1: continue
        if dfs(i, set([i])):
            ans += 1

    return ans, matching

def hungarian_bfs(edges):
    node = preprocess(edges)
    n = len(node)
    matching = [-1] * n
    ans = 0
    for i in xrange(n):
        if matching[i] != -1: continue
        queue = collections.deque([i])
        visited = set()
        prev = {i:-1} # start point
        found = False
        
        while queue and not found:
            x = queue.popleft()
            for neighbor in node[x]:
                if neighbor in visited: continue
                visited.add(neighbor)
                
                if matching[neighbor] != -1:
                    prev[matching[neighbor]] = x
                    queue.append(matching[neighbor])
                else:
                    found = True
                    d, e = x, neighbor
                    while d != -1:
                        t = matching[d]
                        matching[d], matching[e] = e, d
                        d = prev[d]
                        e = t # prev[matching[d]]
                    break


        if matching[i] != -1: ans += 1
    return ans, matching


# print hungarian_dfs([[0,4],[0,6],[1,4],[2,4],[2,5],[3,6],[3,7]])
print hungarian_bfs([[0,4],[0,6],[1,4],[2,4],[2,5],[3,6],[3,7]])