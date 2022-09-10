'''
https://leetcode.com/problems/path-sum-iv
https://leetcode.com/articles/path-sum-iv

If the depth of a tree is smaller than 5, then this tree can be represented by a list of three-digits integers.

For each integer in this list:

The hundreds digit represents the depth D of this node, 1 <= D <= 4.
The tens digit represents the position P of this node in the level it belongs to, 1 <= P <= 8. The position is the same as that in a full binary tree.
The units digit represents the value V of this node, 0 <= V <= 9.
Given a list of ascending three-digits integers representing a binary with the depth smaller than 5. You need to return the sum of all paths from the root towards the leaves.

Example 1:

Input: [113, 215, 221]
Output: 12
Explanation: 
The tree that the list represents is:
    3
   / \
  5   1

The path sum is (3 + 5) + (3 + 1) = 12.
Example 2:

Input: [113, 221]
Output: 4
Explanation: 
The tree that the list represents is: 
    3
     \
      1

The path sum is (3 + 1) = 4.
'''
import math
class Solution(object):
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        levels = [[-1 for _ in xrange(int(math.pow(2,i-1)))] for i in xrange(1,5)]
        
        max_level = 0
        for num in nums:
            level, pos, value = [int(i) for i in str(num)]
            levels[level-1][pos-1] = value
            max_level = max(max_level, level)
        
        ans = 0
        for i in xrange(1, max_level):
            level = levels[i]
            for j in xrange(len(level)):
                if level[j] == -1: continue
                level[j] += levels[i-1][j//2]
                if i+1 >= max_level or levels[i+1][j*2] == -1 and levels[i+1][j*2+1] == -1:
                    ans += level[j]

        return ans if ans > 0 else max(ans, levels[0][0])

s = Solution()
print s.pathSum([]) == 0
print s.pathSum([113]) == 3
print s.pathSum([113, 215]) == 8
print s.pathSum([113, 221]) == 4
print s.pathSum([113, 215, 221]) == 12
print s.pathSum([111,211,313,325,416,447]) == 25
print s.pathSum([111,221,343,486]) == 11
print s.pathSum([111,217,221,315,415]) == 20
print s.pathSum([111,217,221,315,326,415]) == 34
print s.pathSum([111,210,221,315,326,415]) == 20







