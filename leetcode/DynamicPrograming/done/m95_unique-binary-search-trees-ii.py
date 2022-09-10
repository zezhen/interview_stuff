'''
https://leetcode.com/problems/unique-binary-search-trees-ii/description/

Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    # can use memo to improve the performance
    
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n <= 0:
            return []
            
        self.result = []
        nums = range(1, n+1)
        return self.build(nums, 0, n-1)
        
    def build(self, nums, start, end):
        if start > end:
            return [None]
        if start == end:
            return [TreeNode(nums[start])]
        
        result = []
        for i in range(start, end+1):
            lefts = self.build(nums, start, i-1)
            rights = self.build(nums, i+1, end)
            
            for left in lefts:
                for right in rights:
                    root  = TreeNode(nums[i])
                    root.left = left
                    root.right = right
                    result.append(root)
        
        return result