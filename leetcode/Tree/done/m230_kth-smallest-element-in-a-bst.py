'''
https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 <= k <= BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # preorder and stop at kth.
        # Follow up:
        # if BST is modified (insert/delete operations), include a parent pointer for each node
        # maintain the kth pointer, modify accodingly after insering or deleting node.

        node, queue, sequence = root, [], 0
        
        while node or len(queue) > 0:
            while node:
                queue.append(node)
                node = node.left
            
            if len(queue) > 0:
                node = queue.pop()
                sequence += 1
                if sequence == k:
                    return node.val
                node = node.right