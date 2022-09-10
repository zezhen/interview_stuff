'''
https://leetcode.com/problems/redundant-connection-ii/description/

In this problem, a rooted tree is a directed graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.

The given input is a directed graph that started as a rooted tree with N nodes (with distinct values 1, 2, ..., N), with one additional directed edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] that represents a directed edge connecting nodes u and v, where u is a parent of child v.

Return an edge that can be removed so that the resulting graph is a rooted tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array.

Example 1:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given directed graph will be like this:
  1
 / \
v   v
2-->3
Example 2:
Input: [[1,2], [2,3], [3,4], [4,1], [1,5]]
Output: [4,1]
Explanation: The given directed graph will be like this:
5 <- 1 -> 2
     ^    |
     |    v
     4 <- 3
Note:
The size of the input 2D-array will be between 3 and 1000.
Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.
'''

class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        # There are two cases for the tree structure to be invalid.
        # 1) A node having two parents;
        #    including corner case: e.g. [[4,2],[1,5],[5,2],[5,3],[2,4]]
        # 2) A circle exists


        # 1) Check whether there is a node having two parents. 
        #     If so, store them as candidates A and B, and set the second edge invalid. 
        # 2) Perform normal union find. 
        #     If the tree is now valid 
        #        simply return candidate B
        #     else if candidates not existing 
        #        we find a circle, return current edge; 
        #     else 
        #        remove candidate A instead of B.

        c1, c2, parent = None, None, {}
        for a, b in edges:
            if b in parent: # a has two parents
                c1, c2 = [parent[b], b], [a, b]
                break
            parent[b] = a
        
        # union find
        root = list(range(len(edges) + 1))
        
        def find(x):
            while root[x] != x:
                root[x] = root[root[x]]
                x = root[x]
            return root[x]
        
        for a, b in edges:
            if [a, b] == c2: continue
            rA, rB = find(a), find(b)
            if rA == rB: 
                if not c1: return [a, b]
                else: return c1
            root[rA] = root[rB]
        return c2
