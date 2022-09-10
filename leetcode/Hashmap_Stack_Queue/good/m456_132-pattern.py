'''
https://leetcode.com/problems/132-pattern
https://leetcode.com/articles/132-pattern

Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such
that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.

Note: n will be less than 15,000.

Example 1:

Input: [1, 2, 3, 4]

Output: False

Explanation: There is no 132 pattern in the sequence.



Example 2:

Input: [3, 1, 4, 2]

Output: True

Explanation: There is a 132 pattern in the sequence: [1, 4, 2].



Example 3:

Input: [-1, 3, 2, 0]

Output: True

Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].

'''
class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # credit to https://leetcode.com/problems/132-pattern/discuss/94071
        import sys
        stack = []
        s3 = -sys.maxint
        for n in nums[::-1]:
            if n < s3:
                return True
            while stack and stack[-1] < n:
                s3 = stack.pop()
            stack.append(n)
        return False

s = Solution()
print s.find132pattern([1,2]) == False
print s.find132pattern([1,2,3,4]) == False
print s.find132pattern([3,1,4,2]) == True
print s.find132pattern([-1,3,2,0]) == True
