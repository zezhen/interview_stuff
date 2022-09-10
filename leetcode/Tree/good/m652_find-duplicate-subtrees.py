'''
https://leetcode.com/problems/find-duplicate-subtrees
https://leetcode.com/articles/find-duplicate-subtrees
Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.

Example 1: 


        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4


The following are two duplicate subtrees:


      2
     /
    4


and


    4

Therefore, you need to return above trees' root in the form of a list.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # my solution takes too much times, check others solition below, using preorder, amazing

    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        
        # for one node, it's possible duplicated tree can only happened in its parent's another subtree
        if not root: return []

        duplicated = {}
        memo = {}
        def search(p, q):
            if not p and not q: return True
            if (p, q) in memo: return memo[(p, q)]

            flag = False
            if p and q:
                if p.val == q.val and search(p.left, q.left) and search(p.right, q.right):
                    if p not in duplicated and p not in duplicated:
                        s = set([p, q])
                        duplicated[p] = duplicated[q] = s
                    elif p not in duplicated:
                        duplicated[q].add(p)
                        duplicated[p] = duplicated[q]
                    elif q not in duplicated:
                        duplicated[p].add(q)
                        duplicated[q] = duplicated[p]
                    else:
                        s = duplicated[p] | duplicated[q]
                        duplicated[q] = duplicated[p] = s
                    flag = True
                
                search(p, q.left)
                search(p, q.right)
                search(p.left, q)
                search(p.right, q)

            if p:
                search(p.left, p.right)

            if q and not flag:
                search(q.left, q.right)

            memo[(q, p)] = flag
            memo[(p, q)] = flag
            return flag

        search(root.left, root.right)
        # print duplicated

        ans = []
        visited = set()
        for k,v in duplicated.iteritems():
            if k in visited: continue
            ans.append(k)
            visited |= v

        return ans

import sys
sys.path.append('../')
import helper

s = Solution()

# print map(lambda t: helper.tree2array(t), s.findDuplicateSubtrees(helper.array2tree([1,2,3,4,None,2,4,None,None,4])))
# print map(lambda t: helper.tree2array(t), s.findDuplicateSubtrees(helper.array2tree([1,2,2,3,3,3,3,4,None,4,None,4,None,4,None])))
# print map(lambda t: helper.tree2array(t), s.findDuplicateSubtrees(helper.array2tree([1,2,2,3,3,3,3,4,None,5,None,4,None,5,None])))
# print map(lambda t: helper.tree2array(t), s.findDuplicateSubtrees(helper.array2tree([1,2,2,3,5,3,5,4,None,6,None,4,None,6,None])))

# print map(lambda t: helper.tree2array(t), s.findDuplicateSubtrees(helper.array2tree([1]*100)))


print map(lambda t: helper.tree2array(t), s.findDuplicateSubtrees(helper.array2tree([42,10,11,60,65,50,98,66,84,35,97,-6,None,-1,73,2,61,8,20,11,21,13,50,88,89,20,59,65,66,None,81,-7,12,20,-5,82,-8,96,44,58,91,31,65,29,3,93,74,None,None,10,-4,91,55,85,20,52,18,None,None,11,6,91,6,58,82,None,None,21,None,84,None,7,31,None,-9,57,32,94,61,44,61,35,31,-7,54,15,75,21,-9,65,57,74,None,-2,89,24,6,95,None,None,47,None,None,79,None,36,31,79,86,9,5,86,92,-4,83,76,3,24,10,1,10,72,95,43,0,None,38,41,40,-6,10,93,62,94,82,4,-3,25,91,19,36,None,95,37,67,13,15,18,39,57,13,64,50,None,None,26,-3,-7,99,None,-9,77,16,91,9,None,None,None,26,None,78,83,19,76,92,74,96,46,14,None,None,8,98,None,None,26,None,-7,64,39,91,79,60,80,10,3,-2,29,85,53,70,50,24,None,56,None,None,33,None,-5,71,8,62,72,35,83,None,None,None,14,85,-5,17,None,5,2,14,-8,3,73,49,None,89,None,84,None,85,-3,16,8,-9,None,None,91,18,76,None,5,58,58,4,None,None,None,None,95,None,-3,82,99,6,None,None,49,58,-3,54,91,63,None,12,None,26,34,64,93,None,None,None,None,25,-9,91,64,33,76,27,None,None,80,None,None,None,50,68,None,None,None,10,None,None,60,None,None,50,8,None,30,35,36,5,17,22,61,38,40,None,12,98,68,65,60,48,None,20,44,20,59,78,10,91,81,8,3,27,61,None,69,None,53,None,None,None,None,None,92,None,None,None,99,91,15,71,21,66,37,5,None,None,None,12,52,None,None,7,69,28,None,None,68,13,94,76,None,None,None,82,-7,94,None,None,None,42,None,3,None,22,None,25,None,89,99,None,74,60,93,25,75,56,None,14,None,1,24,6,None,None,None,None,-1,None,None,66,3,73,91,60,None,None,16,42,17,81,14,96,33,None,55,None,None,-9,67,4,9,53,None,None,None,None,None,None,None,None,None,42,96,None,29,16,59,None,-3,56,90,None,72,None,None,87,None,None,None,None,None,None,None,None,None,75,None,None,54,None,4,39,-2,None,44,80,14,None,95,8,76,19,None,None,None,None,None,None,None,66,None,68,92,94,5,8,96,None,80,None,None,None,40,52,30,-7,85,None,72,90,1,44,4,59,19,None,None,None,-9,-8,32,63,1,None,25,None,21,33,37,96,-1,43,None,83,80,65,68,99,88,None,48,77,14,None,14,8,None,None,None,None,None,None,None,None,None,89,None,None,14,None,37,None,None,None,None,None,None,None,20,None,None,None,61,20,None,None,None,34,50,53,None,None,51,None,98,25,42,77,59,36,18,68,4,-5,36,71,None,37,78,None,None,None,None,None,None,None,None,None,None,44,74,92,None,None,3,21,76,32,79,None,59,3,86,-9,81,-4,None,None,None,31,61,32,None,None,98,None,-8,5,64,None,43,32,None,78,None,36,None,None,None,48,None,None,None,78,71,None,71,80,12,None,None,None,None,None,29,52,1,83,5,95,2,56,93,65,86,95,None,None,None,None,58,7,None,20,-2,84,None,-9,13,None,None,33,None,58,None,None,0,38,None,None,-9,None,88,None,78,24,None,14,None,None,9,75,53,-3,None,88,71,84,76,62,85,53,None,None,None,79,36,-5,None,91,57,17,None,None,None,None,36,12,-7,51,63,-3,77,40,13,17,10,5,89,-4,72,27,53,None,83,65,None,None,None,None,None,33,None,96,None,None,85,60,9,38,23,None,None,None,39,None,None,None,16,85,99,51,None,None,None,None,None,None,54,None,None,62,None,None,57,90,61,99,69,2,23,71,35,None,-4,51,-1,None,30,3,None,None,17,42,None,None,77,95,39,85,None,-8,43,5,86,None,33,56,47,78,9,70,57,3,29,71,None,None,None,None,None,None,None,None,47,92,85,38,-3,None,None,22,None,None,34,37,None,86,79,68,84,None,None,None,None,None,None,None,78,58,None,None,49,None,None,11,None,None,None,None,None,None,None,88,65,None,50,None,52,None,55,None,13,0,None,None,None,None,30,86,60,68,48,85,None,None,None,20,None,None,None,39,52,77,62,None,82,-6,None,None,60,None,71,None,None,None,39,0,53,None,None,11,None,None,None,3,85,3,78,None,78,-1,30,72,None,None,None,None,35,29,40,79,86,12,21,None,48,46,70,98,62,22,93,None,None,None,None,None,None,None,45,None,None,None,None,None,-6,None,None,None,None,71,None,None,None,None,68,None,41,93,None,None,62,78,-7,14,None,19,16,91,None,None,None,None,None,20,90,51,42,None,None,93,85,None,None,58,9,None,-3,27,86,42,None,None,None,None,None,17,None,None,None,None,22,-8,93,8,49,90,None,None,63,19,39,None,None,None,17,4,54,8,-5,76,None,None,-9,-6,None,34,None,51,10,20,None,23,14,91,26,47,None,47,67,None,None,26,None,None,None,None,None,None,None,None,34,None,15,0,85,13,3,88,86,None,80,39,33,None,52,None,None,39,None,-4,21,None,None,None,2,89,None,None,-1,-6,None,17,-1,65,None,None,None,None,None,19,None,None,63,None,None,None,None,None,-1,68,None,None,None,None,None,None,None,None,17,None,None,None,93,42,None,None,None,12,None,None,None,92,85,82,8,None,None,34,18,90,50,None,99,89,None,19,None,None,78,None,74,-2,None,None,None,63,None,None,38,38,None,None,None,None,None,None,None,None,None,None,74,None,8,None,None,None,49,None,None,None,21,0,None,2,60,15,36,83,59,54,None,-3,None,None,None,-8,None,5,49,32,None,None,None,None,None,7,None,None,None,55,None,None,26,78,98,None,None,57,None,None,83,63,None,None,None,None,81,None,None,33,None,None,None,None,None,None,16,14,None,None,-4,44,None,None,37,16,16,33,None,84,None,25,10,None,None,30,None,None,None,None,None,None,65,None,None,None,93,None,None,None,44,57,12,52,-4,67,None,49,None,None,None,None,None,None,None,64,17,None,None,None,83,4,61,75,None,None,None,None,None,None,24,None,78,-7,None,-5,None,None,30,79,None,44,94,55,14,59,None,None,None,None,None,None,60,None,None,None,None,25,None,None,None,None,97,34,None,None,None,None,80,67,0,None,22,None,96,None,None,None,None,None,None,None,None,47,None,None,None,None,89,None,None,None,None,43,64,None,None,9,None,None,96,37,79,None,None,None,28,81,None,None,5,None,None,7,96,41,82,-6,20,None,None,None,8,None,None,None,None,None,None,None,None,None,82,8,None,None,None,None,None,None,None,None,39,6,None,None,None,None,90,59,-8,None,None,None,None,None,23,None,None,None,15,89,None,None,86,50,40,70,None,None,32,None,None,None,44,-2,None,38,39,None,None,None,None,None,None,None,None,None,2,None,None,None,None,2,None,None,65,47,None,None,62,27,62,38,31,27,None,None,37,None,None,None,None,None,None,None,62,74,86,-7,None,23,None,None,56,None,None,None,6,None,86,72,30,None,None,21,41,92,None,None,None,None,22,None,74,96,87,None,None,None,None,None,-7,None,51,34,80,None,None,None,None,None,None,None,16,20,None,None,15,81,None,55,None,61,None,None,22,None,5,14,None,34,23,None,30,None,6,64,2,65,None,54,None,None,14,None,0,None,None,None,26,None,None,78,None,49,None,None,13,None,None,None,43,None,None,-1,41,33,None,5,78,None,None,None,None,None,None,None,None,None,None,75,None,None,None,None,None,None,63,70,None,None,None,None,None,40,None,None,None,66,None,None,15,None,7,43,None,60,12,None,None,None,None,None,None,None,19,None,74,-5,55,None,None,None,None,52,-4,-5,None,None,None,65,None,None,67,None,3,None,None,95,None,None,36,None,81,None,None,None,None,None,88,74,None,67,None,None,None,None,68,None,None,None,None,52,None,None,82,90,75,25,None,23,None,68,6,11,None,59,None,None,None,None,None,None,None,None,-2,None,None,None,61,None,None,None,32,80,None,None,None,51,6,None,91,None,None,37,None,26,None,78,None,None,None,None,None,None,None,34,None,None,None,None,None,None,24,31,None,None,99,56,None,None,62,12,43,None,None,None,None,None,None,33,None,68,None,None,None,None,53,4,65,4,None,86,None,46,-9,None,None,83,None,None,None,None,93,None,None,78,None,63,None,None,None,None,None,67,None,None,None,None,72,93,25,None,None,27,None,None,92,44,None,None,None,None,2,9,31,None,None,73,92,62,86,None,None,-6,None,None,None,None,58,None,None,None,None,None,None,None,None,54,None,None,None,None,None,None,None,None,16,None,None,None,None,None,None,None,None,None,None,None,28,None,48,None,None,None,None,None,26,None,None,None,None,None,None,37,66,None,None,92,None,None,None,None,86,89,None,None,None,None,None,None,5,85,None,None,75,None,35,None,None,None,None,None,None,None,27,None,None,None,None,None,None,67,84,94,44,None,None,None,None,None,None,None,None,None,None,70,None,None,49,None,None,16,None,None,None,None,None,None,None,87,None,-7,52,None,None,None,67,None,None,None,None,None,None,None,None,None,None,None,None,None,None,80,None,76,None,25,None,91,None,12,41,None,None,26,None,None,None,None,None,None,None,None,None,None,None,None,None,None,94])))





# public List<TreeNode> findDuplicateSubtrees(TreeNode root) {
#     List<TreeNode> res = new LinkedList<>();
#     preorder(root, new HashMap<>(), res);
#     return res;
# }

# public String preorder(TreeNode cur, Map<String, Integer> map, List<TreeNode> res) {
#     if (cur == null) return "#";  
#     String serial = cur.val + "," + preorder(cur.left, map, res) + "," + preorder(cur.right, map, res);
#     if (map.getOrDefault(serial, 0) == 1) res.add(cur);
#     map.put(serial, map.getOrDefault(serial, 0) + 1);
#     return serial;
# }

# and another detail analysis https://leetcode.com/problems/find-duplicate-subtrees/discuss/106016/O(n)-time-and-space-lots-of-analysis