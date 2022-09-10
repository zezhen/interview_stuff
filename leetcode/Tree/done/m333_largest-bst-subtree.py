'''
https://leetcode.com/problems/largest-bst-subtree

Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree with largest number of nodes in it.

Note:
A subtree must include all of its descendants.

Example:

Input: [10,5,15,1,8,null,7]

   10 
   / \ 
  5  15 
 / \   \ 
1   8   7

Output: 3
Explanation: The Largest BST Subtree in this case is the highlighted one.
             The return value is the subtree's size, which is 3.
Follow up:
Can you figure out ways to solve it with O(n) time complexity?

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0

        self.ans = 1 # leaf node is a BST, minimum size is 1
        def search(node):
            # return flag, min_val, max_val, size
            flag, min_val, max_val, size = True, node.val, node.val, 1
            if not node.right and not node.left: return (flag, min_val, max_val, size)

            if node.left:
                lflag, lmin_val, lmax_val, lsize = search(node.left)
                # print node.val, 'l', lflag, lmin_val, lmax_val, lsize
                if not lflag or lmax_val >= node.val: 
                    flag = False
                else:
                    min_val = lmin_val
                    size += lsize

            if node.right:
                rflag, rmin_val, rmax_val, rsize = search(node.right)
                # print node.val, 'r', rflag, rmin_val, rmax_val, rsize
                if not rflag or rmin_val <= node.val: 
                    flag = False
                else:
                    max_val = rmax_val
                    size += rsize
            
            if flag:
                self.ans = max(self.ans, size)
                return True, min_val, max_val, size
            else:
                return False,0,0,0

        search(root)
        return self.ans

import sys
sys.path.append('../')
import helper

s = Solution()

assert s.largestBSTSubtree(helper.array2tree([])) == 0
assert s.largestBSTSubtree(helper.array2tree([1])) == 1
assert s.largestBSTSubtree(helper.array2tree([1,None,3])) == 2
assert s.largestBSTSubtree(helper.array2tree([2,1])) == 2

assert s.largestBSTSubtree(helper.array2tree([10,5,15,1,8,None,7])) == 3
assert s.largestBSTSubtree(helper.array2tree([8,7,9,6,8,8,10])) == 3
assert s.largestBSTSubtree(helper.array2tree([8,7,9,6,None,None,10])) == 5

assert s.largestBSTSubtree(helper.array2tree(range(10000))) == 1

assert s.largestBSTSubtree(helper.array2tree([1,None,3,None,5,None,7,None,9])) == 5
assert s.largestBSTSubtree(helper.array2tree([1,None,3,None,5,6,7,None,9])) == 2

assert s.largestBSTSubtree(helper.array2tree([1,3,2,4,None,None,5])) == 2


