'''
https://leetcode.com/problems/find-leaves-of-binary-tree

Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.

 

Example:

Input: [1,2,3,4,5]
  
          1
         / \
        2   3
       / \     
      4   5    

Output: [[4,5,3],[2],[1]]
 

Explanation:

1. Removing the leaves [4,5,3] would result in this tree:

          1
         / 
        2          
 

2. Now removing the leaf [2] would result in this tree:

          1          
 

3. Now removing the leaf [1] would result in the empty tree:

          []         

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        ans = []
        def find(node, i):
            if not node.left and not node.right:
                if i >= len(ans): ans.append([])
                ans[i].append(node.val)
                return i + 1

            l = find(node.left, i) if node.left else i
            r = find(node.right, i) if node.right else i
            j = max(l, r)
            if j >= len(ans): ans.append([])
            ans[j].append(node.val)
            return j + 1

        find(root, 0)
        return ans

import sys
sys.path.append('../')
import helper

s = Solution()

assert s.findLeaves(helper.array2tree([1,2,3,4,5])) == [[4, 5, 3], [2], [1]]
assert s.findLeaves(helper.array2tree([1,2,7,3,6,None,None,4,5])) == [[4, 5, 6, 7], [3],[2], [1]]
assert s.findLeaves(helper.array2tree(range(10))) == [[7,8,9,5,6], [3,4,2], [1],[0]]

