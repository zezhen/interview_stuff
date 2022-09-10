'''
https://leetcode.com/problems/shortest-path-visiting-all-nodes
https://leetcode.com/articles/shortest-path-visiting-all-nodes
An undirected, connected graph of N nodes (labeled 0, 1, 2, ..., N-1) is given as graph.

graph.length = N, and j != i is in the list graph[i] exactly once, if and only if nodes i and j are connected.

Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.

 




Example 1:


Input: [[1,2,3],[0],[0],[0]]
Output: 4
Explanation: One possible path is [1,0,2,0,3]

Example 2:


Input: [[1],[0,2,4],[1,3,4],[2],[1,2]]
Output: 4
Explanation: One possible path is [0,1,4,2,3]


 

Note:


	1 <= graph.length <= 12
	0 <= graph[i].length < graph.length

'''
import collections
class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        
        queue = collections.deque()
        visited = set()
        
        for i in xrange(len(graph)):
            bitmask = 1 << i
            queue.append((i, bitmask, 0))   # start_index, bitmask, cost
            visited.add((i, bitmask))       # current_index, bitmask
        
        while queue:
            index, bitmask, cost = queue.popleft()
            # print index, bitmask, cost
            
            # BFS guarantee the first one reach 2^N-1 is the shotest one
            if bitmask == (1 << len(graph)) - 1:
                return cost
            
            for neighbor in graph[index]:
                bm = bitmask | (1 << neighbor)
                if (neighbor, bm) not in visited:
                    visited.add((neighbor, bm))
                    queue.append((neighbor, bm, cost+1))
            