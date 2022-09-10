'''
https://leetcode.com/problems/closest-leaf-in-a-binary-tree
https://leetcode.com/articles/closest-leaf-in-binary-tree

Given a binary tree where every node has a unique value, and a target key k, find the value of the nearest leaf node to target k in the tree.

Here, nearest to a leaf means the least number of edges travelled on the binary tree to reach any leaf of the tree. Also, a node is called a leaf if it has no children.

In the following examples, the input tree is represented in flattened form row by row. The actual root tree given will be a TreeNode object.

Example 1:

Input:
root = [1, 3, 2], k = 1
Diagram of binary tree:
          1
         / \
        3   2

Output: 2 (or 3)

Explanation: Either 2 or 3 is the nearest leaf node to the target of 1.
Example 2:

Input:
root = [1], k = 1
Output: 1

Explanation: The nearest leaf node is the root node itself.
Example 3:

Input:
root = [1,2,3,4,null,null,null,5,null,6], k = 2
Diagram of binary tree:
             1
            / \
           2   3
          /
         4
        /
       5
      /
     6

Output: 3
Explanation: The leaf node with value 3 (and not the leaf node with value 6) is nearest to the node with value 2.
Note:

root represents a binary tree with at least 1 node and at most 1000 nodes.
Every node has a unique node.val in range [1, 1000].
There exists some node in the given binary tree for which node.val == k.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys
class Solution(object):
  def findClosestLeaf_fastest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        mapper = dict() # point to parent node
        def dfs(node):
            if not node:
                return None
            if node.val == k:
                return node
            if node.left:
                mapper[node.left.val] = node
            if node.right:
                mapper[node.right.val] = node
            return dfs(node.left) or dfs(node.right)
        knode = dfs(root)
        queue = [knode]
        visited = set()
        visited.add(knode)
        while queue:
            curr = queue.pop(0)
            if not curr.left and not curr.right:
                return curr.val
            if curr.left and curr.left not in visited:
                visited.add(curr.left)
                queue.append(curr.left)
            if curr.right and curr.right not in visited:
                visited.add(curr.right)
                queue.append(curr.right)
            if curr.val in mapper:
                visited.add(mapper[curr.val])
                queue.append(mapper[curr.val])

    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        memo = {}
        def flow_up(node):
            if not node.left and not node.right: 
                memo[node] = (0, node.val)
                return memo[node]

            ld = sys.maxint
            if node.left:
                ld, ln = flow_up(node.left)

            rd = sys.maxint
            if node.right:
                rd, rn = flow_up(node.right)

            if ld > rd:
                memo[node] = (rd + 1, rn)
            else:
                memo[node] = (ld + 1, ln)
            
            return memo[node]

        def press_down(node, dist, k):
            
            if node.left:
                if node.left.val == k:
                    if dist + 1 < memo[node.left][0]:
                        return memo[node][1]
                    else:
                        return memo[node.left][1]
                else:
                    res = press_down(node.left, min(dist + 1, memo[node.left][0]), k)
                    if res: return res
            if node.right:
                if node.right.val == k:
                    if dist + 1 < memo[node.right][0]:
                        return memo[node][1]
                    else:
                        return memo[node.right][1]
                else:
                    res = press_down(node.right, min(dist + 1,memo[node.right][1]), k)
                    if res: return res

            return None

        

        dist, leaf = flow_up(root)
        if root.val == k: return leaf

        return press_down(root, dist, k)

import sys
sys.path.append('../')
import helper

s = Solution()
print s.findClosestLeaf(helper.array2tree([1,3,2]), 1) == 3
print s.findClosestLeaf(helper.array2tree([1,3,2]), 2) == 2
print s.findClosestLeaf(helper.array2tree([1,3,2]), 3) == 3

print s.findClosestLeaf(helper.array2tree([1,2,3,4,None,None,None,5,None,6]),1) == 3
print s.findClosestLeaf(helper.array2tree([1,2,3,4,None,None,None,5,None,6]),2) == 3
print s.findClosestLeaf(helper.array2tree([1,2,3,4,None,None,None,5,None,6]),3) == 3
print s.findClosestLeaf(helper.array2tree([1,2,3,4,None,None,None,5,None,6]),4) == 6
print s.findClosestLeaf(helper.array2tree([1,2,3,4,None,None,None,5,None,6]),5) == 6
print s.findClosestLeaf(helper.array2tree([1,2,3,4,None,None,None,5,None,6]),6) == 6

print s.findClosestLeaf(helper.array2tree([1,2,3,4,None,None,7,8,9,None,None,12,None,None,None,None,13,None,14]),8) == 9

print s.findClosestLeaf(helper.array2tree([1,2,3,4,5]),5) == 5


