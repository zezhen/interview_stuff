'''
https://leetcode.com/problems/house-robber-iii
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:


Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

Output: 7 
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Example 2:


Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \ 
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        memo = {}
        def _rob(node, skip):
            if not node: return 0

            if (node, skip) in memo:
                return memo[(node, skip)]

            if skip:
                res = _rob(node.left, False) + _rob(node.right, False)
                memo[(node, skip)] = res
                return res

            res = max(node.val + _rob(node.left, True) + _rob(node.right, True), _rob(node.left, False) + _rob(node.right, False))
            memo[(node, skip)] = res
            return res

        return _rob(root, False)

import sys
sys.path.append('../')
import helper

s = Solution()

print s.rob(helper.array2tree([3,4,5,1,3,None,1])) == 9
print s.rob(helper.array2tree(range(1,11))) == 42