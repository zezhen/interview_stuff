'''
https://leetcode.com/problems/binary-tree-inorder-traversal
https://leetcode.com/articles/binary-tree-inorder-traversal
Given a binary tree, return the inorder traversal of its nodes' values.

Example:


Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]

Follow up: Recursive solution is trivial, could you do it iteratively?
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        node, candidates, ret = root, [], []
        
        while node or len(candidates) > 0:
            while node:
                candidates.append(node)
                node = node.left
            
            if len(candidates) > 0:
                node = candidates.pop()
                ret.append(node.val)
                node = node.right
        
        return ret