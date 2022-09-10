'''
https://leetcode.com/problems/range-sum-of-bst
https://leetcode.com/articles/range-sum-of-bst
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

 


Example 1:


Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32



Example 2:


Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23


 

Note:


	The number of nodes in the tree is at most 10000.
	The final answer is guaranteed to be less than 2^31.


'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        
        ans = 0
        node, queue = root, deque()
        while node or len(queue) > 0:
            while node:
                queue.append(node)
                node = node.left if node.val > L else None

            if len(queue) > 0:
                node = queue.pop()
                ans += node.val if L <= node.val <= R else 0
                node = node.right if node.val < R else None

        return ans


import sys
sys.path.append('../')
import helper

s = Solution()
print s.rangeSumBST(helper.array2tree([10,5,15,3,7,None,18]), 0, 7) == 15
print s.rangeSumBST(helper.array2tree([10,5,15,3,7,None,18]), 7, 15) == 32
print s.rangeSumBST(helper.array2tree([10,5,15,3,7,None,18]), 18, 30) == 18
print s.rangeSumBST(helper.array2tree([10,5,15,3,7,None,18]), 19, 30) == 0

print s.rangeSumBST(helper.array2tree([10,5,15,3,7,13,18,1,None,6]), 6, 10) == 23
print s.rangeSumBST(helper.array2tree([10,5,15,3,7,13,18,1,None,6]), 1, 1) == 1