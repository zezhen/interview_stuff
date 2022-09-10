'''
https://leetcode.com/problems/count-complete-tree-nodes/description/

Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import math
class Solution(object):
    '''
    what's the trick here? Stop condition

    1. check left tree, if it's not complete tree, then skip right
    2. if both side are complete, then compare the height

    '''
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        _, ans, _ = self._count(root, 0)
        return ans

    def _count(self, root, level):
            
        if not root.left and not root.right:
            return (level, 1, False)

        if root.left and not root.right:
            return (level+1, 2, True)
        
        llevel, lcount, ldone = self._count(root.left, level + 1)
        if ldone:
            rcount = int(math.pow(2, llevel - level - 1)) - 1
            return (llevel, lcount + rcount + 1, True)

        rlevel, rcount, rdone = self._count(root.right, level + 1)
        if rdone or llevel > rlevel:
            return (llevel, lcount + rcount + 1, True)
        
        return (rlevel, lcount + rcount + 1, False)
        
    # fast solution
    def countNodes2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        height = -1
        temp = root
        while temp != None:
            height+=1
            temp = temp.left
        if height == -1:
            return 0
        if height == 0:
            return 1
        nodes = 0
        
        while height >= 0:
            if height == 0:
                nodes +=1
                break
            temp = root.right
            h = -1
            while temp != None:
                h+=1
                temp = temp.left
            nodes = nodes + 2**(h+1)    
            if h == height - 1:     # 2**(h+1) is the left subtree + root node, continue right subtree
                root = root.right
            else:                   # 2**(h+1) is the right subtree + root node, continue left subtree
                root = root.left
            height -=1
            
        return nodes