'''
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).


For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7



return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    # follow the idea in binary-tree-level-order-traversal
    # but add reversed val to ans
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None: return []

        ans, queue = [[root.val]], [root]
        head, tail = 0, len(queue)
        reverse = True
        while head < len(queue):
            node = queue[head]
            head += 1

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            if head == tail:
                tail = len(queue)
                if tail > head:
                    values = map(lambda n:n.val, queue[head:tail])
                    if reverse:
                        values.reverse()
                        reverse = False
                    ans.append(values)
        return ans

    def zigzagLevelOrder1(self, root):
        if not root:
            return []
        
        ret = []
        right, queue = False, [None, root]
        
        while len(queue) > 1:
            node = queue.pop(0)
            if not node:
                item = []
                ret.append(item)
                queue.append(None)
                right = not right
            else:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if right:
                    item.append(node.val)
                else:
                    item.insert(0, node.val)
        return ret
    