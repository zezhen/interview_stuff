'''
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Example 1:

Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4 

Output: 2
Example 2:

Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3

Output:  1
Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
'''
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """

        def find(seq, i):
            while seq[i] != i:
                seq[i] = seq[seq[i]]    # compression
                i = seq[i]
            return i

        def find1(seq, i):
            if seq[i] != i:
                seq[i] = find(seq, seq[i])
            return seq[i]

        seq = range(n)
        for f, t in edges:
            fi = find(seq, f)
            ti = find(seq, t)
            if fi != ti:
                seq[fi] = ti        # union
                n -= 1

        # one more step to make all nodes has same id
        # for i in xrange(n):
        #     find(seq, i)
        # print seq
        return n

    def countComponents_dfs(self, n, edges):
        matrix = [[] for _ in xrange(n)]
        for f, t  in edges:
            matrix[f].append(t)
            matrix[t].append(f)

        count = 0
        visited = [False] * n
        for u in xrange(n):
            if visited[u] == False:
                stack = [u]
                while len(stack) > 0:
                    u = stack.pop()
                    visited[u] = True
                    for v in matrix[u]:
                        if not visited[v]: 
                            stack.append(v)
                count += 1
        print seq
        return count

    def countComponents_tarjan_for_directed_graph(self, n, edges):
        matrix = [[] for _ in xrange(n)]
        for f, t  in edges:
            matrix[f].append(t)
            matrix[t].append(f)

        self.count = 0
        self.seq = 0
        self.stack = []

        dfn = [-1] * n
        low = [-1] * n
        def tarjan(matrix, u, dfn, low):
            self.seq += 1
            dfn[u] = low[u] = self.seq  # dfn is the seq of node visited, 
                                        # low is the minimum seq node u can reach
            self.stack.append(u)
            for v in matrix[u]:
                if dfn[v] == -1:                    # not visited
                    tarjan(matrix, v, dfn, low)     # dfs and check the neighbor v
                    low[u] = min(low[u], low[v])    # u can reach v, thus can reach minimum seq that v reaches.
                elif v in self.stack:
                    low[u] = min(low[u], dfn[v])    # u can reach to v and v is in stack, they're in same component
                                                    # v was visited earlier and might have lower seq, update low[u]
            if dfn[u] == low[u]:
                self.count += 1
                while self.stack.pop() != u: pass

        for i in xrange(n):
            if dfn[i] == -1:
                tarjan(matrix, i, dfn, low)

        return self.count

s = Solution()
# assert s.countComponents(5, [[0, 1], [1, 2], [3, 4]]) == 2
# assert s.countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == 1

assert s.countComponents(4, [[0, 1], [2, 3], [1, 2]]) == 1