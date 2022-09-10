'''
https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii
https://leetcode.com/articles/binary-tree-longest-consecutive-sequence-ii

Given a binary tree, you need to find the length of Longest Consecutive Path in Binary Tree.

Especially, this path can be either increasing or decreasing. For example, [1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is not valid. On the other hand, the path can be in the child-Parent-child order, where not necessarily be parent-child order.

Example 1:

Input:
        1
       / \
      2   3
Output: 2
Explanation: The longest consecutive path is [1, 2] or [2, 1].
Example 2:

Input:
        2
       / \
      1   3
Output: 3
Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].
Note: All the values of tree nodes are in the range of [-1e7, 1e7].
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # try to use iteration but fail to collect full information
    # have to use incursion, but what if tree is deep?
    def longestConsecutive(self, root):
          """
          :type root: TreeNode
          :rtype: int
          """
          def search(node):
              if node == None: return (0, 0, 0)
              if not node.left and not node.right: return (1, 1, 1)

              lincrease, ldecrease, lmax = 0,0,0
              if node.left:
                  lincrease, ldecrease, lmax = search(node.left)
                  
                  lincrease = lincrease +1 if node.val - node.left.val == 1 else 0
                  ldecrease = ldecrease +1 if node.val - node.left.val == -1 else 0

              rincrease, rdecrease, rmax = 0,0,0
              if node.right:
                  rincrease, rdecrease, rmax = search(node.right)

                  rincrease = rincrease +1 if node.val - node.right.val == 1 else 0
                  rdecrease = rdecrease +1 if node.val - node.right.val == -1 else 0

              combine = 0
              if node.left and node.right:
                  combine1 = lincrease + rdecrease - 1 if node.val - node.left.val == node.right.val - node.val == 1 else 0
                  combine2 = ldecrease + rincrease - 1 if node.val - node.left.val == node.right.val - node.val == -1 else 0
                  combine = max(combine1, combine2)

              nodeincrease = max(lincrease, rincrease)
              nodedecrease = max(ldecrease, rdecrease)
              nodemax = max(lmax, rmax, combine)

              return nodeincrease, nodedecrease, nodemax

          return max(search(root))


import sys
sys.path.append('../')
import helper

s = Solution()

assert s.longestConsecutive(helper.array2tree([])) == 0
assert s.longestConsecutive(helper.array2tree([1])) == 1
assert s.longestConsecutive(helper.array2tree([1,2])) == 2
assert s.longestConsecutive(helper.array2tree([1,3])) == 1
assert s.longestConsecutive(helper.array2tree([2,1,3])) == 3
assert s.longestConsecutive(helper.array2tree([1,2,3])) == 2
assert s.longestConsecutive(helper.array2tree([4,3,5,1,2,6,7])) == 5
assert s.longestConsecutive(helper.array2tree([8,7,7,6,8,6,8,5,None,None,9,5,None,None,7])) == 5

