'''
https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/

You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0] 
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.

'''
import bisect
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        queue = []
        ans = []
        for n in nums[::-1]:
            i = bisect.bisect_left(queue, n)
            ans.append(i)
            bisect.insort_left(queue, n)
        return ans[::-1]

s = Solution()
print s.countSmaller([]) == []
print s.countSmaller([5]) == [0]
print s.countSmaller([5,5]) == [0,0]
print s.countSmaller([5,2,6,1]) == [2,1,1,0]
print s.countSmaller(range(10000)) == [0] * 10000
print s.countSmaller(range(10000)[::-1]) == range(10000)[::-1]