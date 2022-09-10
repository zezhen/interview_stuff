'''
https://leetcode.com/problems/number-of-islands-ii

A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example:

Input: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
Output: [1,1,2,3]
Explanation:

Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).

0 0 0
0 0 0
0 0 0
Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

1 0 0
0 0 0   Number of islands = 1
0 0 0
Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

1 1 0
0 0 0   Number of islands = 1
0 0 0
Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

1 1 0
0 0 1   Number of islands = 2
0 0 0
Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

1 1 0
0 0 1   Number of islands = 3
0 1 0
Follow up:

Can you do it in time complexity O(k log mn), where k is the length of the positions?

'''
import collections
class Solution(object):
    # most others' solution is making union-find on positions level
    # increase self.numIslands every time, add into islands array
    # then do the union-find
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        ans = []

        self.numIslands = 0        # distinct island number
        islandId = 0            # incremental island id
        lands = collections.defaultdict(dict)    # record island id according the positions
                                                 # aka. spare 2D array
        islands = collections.deque()            # record the island id here, union find happen here

        def find(_id):
            while _id != islands[_id]:
                islands[_id] = islands[islands[_id]]
                _id = islands[_id]
            return _id

        def union(x,y, i,j):
            id1 = find(lands[x][y])
            id2 = find(lands[i][j])
            if id1 != id2:
                islands[id1] = id2
                lands[x][y] = id2
                self.numIslands -= 1
        
        for x,y in positions:
            self.numIslands += 1
            lands[x][y] = islandId
            islands.append(islandId)
            islandId += 1

            if x > 0 and y in lands[x-1]:
                union(x,y, x-1,y)
            if y > 0 and y-1 in lands[x]:
                union(x,y, x,y-1)
            if x < m-1 and y in lands[x+1]:
                union(x,y, x+1,y)
            if y < n-1 and y+1 in lands[x]:
                union(x,y, x,y+1)
                
            ans.append(self.numIslands)

        return ans

s = Solution()
print s.numIslands2(3,3,[[0,0], [0,1], [1,2], [2,1], [1,1]])
print s.numIslands2(3,3,[[0,1],[1,2],[2,1],[1,0],[0,2],[0,0],[1,1]])