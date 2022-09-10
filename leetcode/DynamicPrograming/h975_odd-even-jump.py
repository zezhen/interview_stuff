'''
https://leetcode.com/problems/odd-even-jump/description/

You are given an integer array A.  From some starting index, you can make a series of jumps.  The (1st, 3rd, 5th, ...) jumps in the series are called odd numbered jumps, and the (2nd, 4th, 6th, ...) jumps in the series are called even numbered jumps.

You may from index i jump forward to index j (with i < j) in the following way:

During odd numbered jumps (ie. jumps 1, 3, 5, ...), you jump to the index j such that A[i] <= A[j] and A[j] is the smallest possible value.  If there are multiple such indexes j, you can only jump to the smallest such index j.
During even numbered jumps (ie. jumps 2, 4, 6, ...), you jump to the index j such that A[i] >= A[j] and A[j] is the largest possible value.  If there are multiple such indexes j, you can only jump to the smallest such index j.
(It may be the case that for some index i, there are no legal jumps.)
A starting index is good if, starting from that index, you can reach the end of the array (index A.length - 1) by jumping some number of times (possibly 0 or more than once.)

Return the number of good starting indexes.

 

Example 1:

Input: [10,13,12,14,15]
Output: 2
Explanation: 
From starting index i = 0, we can jump to i = 2 (since A[2] is the smallest among A[1], A[2], A[3], A[4] that is greater or equal to A[0]), then we can't jump any more.
From starting index i = 1 and i = 2, we can jump to i = 3, then we can't jump any more.
From starting index i = 3, we can jump to i = 4, so we've reached the end.
From starting index i = 4, we've reached the end already.
In total, there are 2 different starting indexes (i = 3, i = 4) where we can reach the end with some number of jumps.
Example 2:

Input: [2,3,1,1,4]
Output: 3
Explanation: 
From starting index i = 0, we make jumps to i = 1, i = 2, i = 3:

During our 1st jump (odd numbered), we first jump to i = 1 because A[1] is the smallest value in (A[1], A[2], A[3], A[4]) that is greater than or equal to A[0].

During our 2nd jump (even numbered), we jump from i = 1 to i = 2 because A[2] is the largest value in (A[2], A[3], A[4]) that is less than or equal to A[1].  A[3] is also the largest value, but 2 is a smaller index, so we can only jump to i = 2 and not i = 3.

During our 3rd jump (odd numbered), we jump from i = 2 to i = 3 because A[3] is the smallest value in (A[3], A[4]) that is greater than or equal to A[2].

We can't jump from i = 3 to i = 4, so the starting index i = 0 is not good.

In a similar manner, we can deduce that:
From starting index i = 1, we jump to i = 4, so we reach the end.
From starting index i = 2, we jump to i = 3, and then we can't jump anymore.
From starting index i = 3, we jump to i = 4, so we reach the end.
From starting index i = 4, we are already at the end.
In total, there are 3 different starting indexes (i = 1, i = 3, i = 4) where we can reach the end with some number of jumps.
Example 3:

Input: [5,1,3,4,2]
Output: 3
Explanation: 
We can reach the end from starting indexes 1, 2, and 4.
 

Note:

1 <= A.length <= 20000
0 <= A[i] < 100000
'''

import bisect
class Solution(object):
    def oddEvenJumps(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        good = [False] * len(A)
        # in python, there is no struct like TreeMap, which the insertion operation is O(logn)
        # here we will use array, and use bisect.insort to update array O(n)
        nums = []
        
        # last number is always good
        good[-1] = (True, True) # odd/even jump
        n = len(A)
        nums.append((A[n-1],n-1))
        
        for i in range(n-1)[::-1]:
            odd_jump = even_jump = False
            j = bisect.bisect_left(nums, (A[i],))

            # odd jump: find the smallest number k >= A[i]
            # even jump: find the largest number k <= A[i]
            even_jump_ind = odd_jump_ind = None

            if j >= len(nums):
                even_jump_ind = j - 1
            elif nums[j][0] == A[i]:
                even_jump_ind = odd_jump_ind = j
            else:
                even_jump_ind = j - 1 if j > 0 else None
                odd_jump_ind = j

            if even_jump_ind != None:
                oj,ej = good[nums[even_jump_ind][1]]
                even_jump = oj
            if odd_jump_ind != None:
                oj,ej = good[nums[odd_jump_ind][1]]
                odd_jump = ej

            good[i] = (odd_jump, even_jump)
            # print i, j, nums, even_jump_ind, odd_jump_ind, good[i]
            
            if j < len(nums) and A[i] == nums[j][0]:
                nums[j] = (A[i], i)
            else:
                bisect.insort(nums, (A[i],i))
        
        # print good
        return len(filter(lambda t:t[0], good))

    def oddEvenJumps_fastest(self, A):
        N = len(A)

        def make(B):
            ans = [None] * N
            stack = []  # invariant: stack is decreasing
            for i in B:
                while stack and i > stack[-1]:
                    ans[stack.pop()] = i
                stack.append(i)
            return ans

        B = sorted(range(N), key = lambda i: A[i])
        oddnext = make(B)
        B.sort(key = lambda i: -A[i])
        evennext = make(B)

        odd = [False] * N
        even = [False] * N
        odd[N-1] = even[N-1] = True

        for i in xrange(N-2, -1, -1):
            if oddnext[i] is not None:
                odd[i] = even[oddnext[i]]
            if evennext[i] is not None:
                even[i] = odd[evennext[i]]

        return sum(odd)
        
        
s = Solution()
print s.oddEvenJumps([10,13,12,14,15]) == 2
print s.oddEvenJumps([2,3,1,1,4]) == 3
print s.oddEvenJumps([5,1,3,4,2]) == 3