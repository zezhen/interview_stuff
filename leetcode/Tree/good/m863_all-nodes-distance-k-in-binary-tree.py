'''
https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree
https://leetcode.com/articles/all-nodes-distance-k-in-binary-tree
We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.

 





Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.



Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.


 

Note:


	The given tree is non-empty.
	Each node in the tree has unique values 0 <= node.val <= 500.
	The target node is a node in the tree.
	0 <= K <= 1000.


'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # dfs + bfs
    def distanceK(self, root, target, K):
        conn = collections.defaultdict(list)    # connect parent and child
        def connect(parent, child):
            if parent and child:
                conn[parent.val].append(child.val)
                conn[child.val].append(parent.val)
            if child.left: connect(child, child.left)
            if child.right: connect(child, child.right)
        connect(None, root)
        bfs = [target.val]
        seen = set(bfs)
        for i in xrange(K):
            bfs = [y for x in bfs for y in conn[x] if y not in seen]
            seen |= set(bfs)
        return bfs

        

        if root == target:
            return searchLevel(root, K)
        else:
            lorR, level = searchTarget(root)
            targetSubtree, oppositeSubtree = (root.left, root.right) if lorR == 0 else (root.right, root.left)
            deep = searchLevel(target, K)
            if K == level:
                return deep + [root]
            elif K > level:
                return deep + searchLevel(oppositeSubtree, K-level+1)
            else:
                return deep + searchLevel(targetSubtree, level - K)
            




