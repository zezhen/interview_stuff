'''
https://leetcode.com/problems/binary-tree-level-order-traversal
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).


For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7



return its level order traversal as:

[
  [3],
  [9,20],
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
    # honestly, level traversal use queue to push/pop is quite ineffecient.
    # we can maintan a queue, but use a pointer to indicate the head position 
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None: return []

        ans, queue = [[root.val]], [root]
        head, tail = 0, len(queue)
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
                    ans.append(map(lambda n:n.val, queue[head:tail]))
        return ans


    def levelOrder1(self, root):        
        if root == None:
            return []
        ret = []

        nodeQueue = [root, None]
        subQueue = []
        ret.append(subQueue)
        while len(nodeQueue) > 1:
            node = nodeQueue.pop(0)
            if node == None:
                subQueue = []
                ret.append(subQueue)
                nodeQueue.append(node)
            else:
                subQueue.append(node.val)
                if node.left != None:
                    nodeQueue.append(node.left)
                if node.right != None:
                    nodeQueue.append(node.right)
        return ret