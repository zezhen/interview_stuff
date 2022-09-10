'''
https://leetcode.com/problems/equal-tree-partition
https://leetcode.com/articles/equal-tree-partition

Given a binary tree with n nodes, your task is to check if it's possible to partition the tree to two trees which have the equal sum of values after removing exactly one edge on the original tree.

Example 1:

Input:     
    5
   / \
  10 10
    /  \
   2   3

Output: True
Explanation: 
    5
   / 
  10
      
Sum: 15

   10
  /  \
 2    3

Sum: 15
Example 2:

Input:     
    1
   / \
  2  10
    /  \
   2   20

Output: False
Explanation: You can't split the tree into two trees with equal sum after removing exactly one edge on the tree.
Note:

The range of tree node value is in the range of [-100000, 100000].
1 <= n <= 10000
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        # record all subtrees' sum into a set tsum
        # total_sum the sum from root
        
        if not root: return False

        tsum = set()
        def sumTree(tree, add=True):
            if not tree: return 0

            _sum = tree.val + sumTree(tree.left) + sumTree(tree.right)
            if add: tsum.add(_sum)
            return _sum

        total_sum = sumTree(root, False)
        if total_sum % 2 != 0: return False
        return (total_sum // 2) in tsum



