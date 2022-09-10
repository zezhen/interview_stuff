'''
https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree

Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.

You may assume each number in the sequence is unique.

Consider the following binary search tree: 

     5
    / \
   2   6
  / \
 1   3
Example 1:

Input: [5,2,6,1,3]
Output: false
Example 2:

Input: [5,2,1,3,6]
Output: true
Follow up:
Could you do it using only constant space complexity?

'''

class Solution(object):

    # good solution
    # Kinda simulate the traversal, keeping a stack of nodes (just their values) of which we're still in the left subtree. If the next number is smaller than the last stack value, then we're still in the left subtree of all stack nodes, so just push the new one onto the stack. But before that, pop all smaller ancestor values, as we must now be in their right subtrees (or even further, in the right subtree of an ancestor). Also, use the popped values as a lower bound, since being in their right subtree means we must never come across a smaller number anymore.
    def verifyPreorder(self, preorder):
        stack = []
        low = float('-inf')
        for p in preorder:
            if p < low:
                return False
            while stack and p > stack[-1]:
                low = stack.pop()
            stack.append(p)
        return True

    # the first number in preorder is the root
    # it could separaet the preorder into two parts, splitted at k:
    # [1:k] < preorder[0] < [k+1:n-1]
    # recursion into [1:k] and [k+1:n-1]

    # worst case is ordered sequence, like [0,1,2,3,4,5]...
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """

        def verify(s, e):
            if s == e: return True

            root = preorder[s]

            l = s + 1
            while l <= e and preorder[l] < root:
                l += 1
            if l > e: return verify(s+1, e)

            r = e
            while r >= s+1 and preorder[r] > root:
                r -= 1

            if r <= s: return verify(s+1, e)

            if l - 1 == r: 
                return verify(s+1, r) and verify(l, e)
            else: 
                return False

        return verify(0, len(preorder) - 1)

s = Solution()
assert s.verifyPreorder([5,2,6,1,3]) == False
assert s.verifyPreorder([5,2,1,3,6]) == True
assert s.verifyPreorder([4,2,1,3,6,5,7]) == True
assert s.verifyPreorder([1,2,3,4,5,6,7,8,9]) == True
assert s.verifyPreorder([9,8,7,6,5,4,3,2,1]) == True
assert s.verifyPreorder([1,2,0]) == False
assert s.verifyPreorder([2,0,1]) == True
assert s.verifyPreorder(range(1000)) == True

