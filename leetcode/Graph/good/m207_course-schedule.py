'''
https://leetcode.com/problems/course-schedule
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:


Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.

Example 2:


Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.


Note:


	The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
	You may assume that there are no duplicate edges in the input prerequisites.

'''

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        
        adjmatrices = [[] for _ in xrange(numCourses)]
        indegree = [0] * numCourses
        for f,t in prerequisites:
            adjmatrices[f].append(t)
            indegree[t] += 1

        visited = [False] * numCourses
        onpath = [False] * numCourses
        def dfs_cycle(adjmatrices, node, visited, onpath):
            if visited[node]: return False

            onpath[node] = visited[node] = True
            for neighbor in adjmatrices[node]:
                if onpath[neighbor] || dfs_cycle(neighbor):
                    return True
            onpath[node] = False
            return False

        def bfs_cycle(adjmatrices, indegree):
            size = len(indegree)
            for i in xrange(size):
                for j in xrange(size):
                    if indegree[j] == 0: break
                else:
                    return True # there is no j that indgree is 0
                indegree[j] = -1 # to prevent visiting it again
                for neighbor in adjmatrices[j]:
                    indegree[neighbor] -= 1
            return False

        def kahn(adjmatrices, indegree):
            from collections import deque
            noincoming = deque()
            ans = []
            size = len(indegree)

            for i in xrange(size):
                if indegree[i] == 0: noincoming.append(i)

            while len(noincoming) > 0:
                node = noincoming.popleft()
                ans.append(node)
                for neighbor in adjmatrices[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        noincoming.append(neighbor)

            if len(ans) != size:
                return 'error:graph has at least onecycle'
            else:
                return ans