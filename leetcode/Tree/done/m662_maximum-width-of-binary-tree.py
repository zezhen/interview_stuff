'''
https://leetcode.com/problems/maximum-width-of-binary-tree
https://leetcode.com/articles/maximum-width-of-binary-tree
Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null. 

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

Example 1:

Input: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).



Example 2:

Input: 

          1
         /  
        3    
       / \       
      5   3     

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).



Example 3:

Input: 

          1
         / \
        3   2 
       /        
      5      

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).


Example 4:

Input: 

          1
         / \
        3   2
       /     \  
      5       9 
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).




Note:
Answer will in the range of 32-bit signed integer.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
          if not root: return 0

          queue = [(root,1)]
          head, tail = 0, len(queue)
          maxWidth = 1
          while head < len(queue):
              node, sid = queue[head]
              head += 1

              if node.left:
                  queue.append((node.left, 2*sid-1))
              if node.right:
                  queue.append((node.right,2*sid))
              if head == tail:
                  tail = len(queue)
                  if tail > head:
                      maxWidth = max(maxWidth, queue[tail-1][1] - queue[head][1] + 1)
          return maxWidth


import sys
sys.path.append('../')
import helper

s = Solution()

assert s.widthOfBinaryTree(helper.array2tree([])) == 0
assert s.widthOfBinaryTree(helper.array2tree([1])) == 1
assert s.widthOfBinaryTree(helper.array2tree([1,2])) == 1
assert s.widthOfBinaryTree(helper.array2tree([1,3,2])) == 2
assert s.widthOfBinaryTree(helper.array2tree([1,3,2,5,3,None,9])) == 4
assert s.widthOfBinaryTree(helper.array2tree([1,3,None,5,3])) == 2
assert s.widthOfBinaryTree(helper.array2tree([1,3,2,5])) == 2
assert s.widthOfBinaryTree(helper.array2tree([1,3,2,5,None,None,9,6,None,None,7])) == 8
assert s.widthOfBinaryTree(helper.array2tree([1,3,2,5,None,None,9,6,None,8,7])) == 8
assert s.widthOfBinaryTree(helper.array2tree([1,3,2,5,None,None,9,None,None,8,7])) == 4



