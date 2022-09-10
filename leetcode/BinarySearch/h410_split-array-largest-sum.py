'''
https://leetcode.com/problems/split-array-largest-sum/description/

Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 <= n <= 1000
1 <= m <= min(50, n)
Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
'''
import bisect
import sys
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        average = sum(nums) / m
        acc = [nums[0]]
        for i in xrange(1, len(nums)):
            acc.append(nums[i] + acc[-1])
        
        ans = 0
        l = 0
        for j in xrange(1, m):
            i = bisect.bisect(acc, j * average, l)
            print 'i', i
            ans = max(ans, sum(nums[l:i]))
            l = i
        print l
        ans = max(ans, sum(nums[l:]))
        return ans

s = Solution()
print s.splitArray([7,2,5,10,8], 2) #== 18
print s.splitArray([1,2,3,4], 2) #== 6

def rand(start=0, end=1, count=1000):
    import random
    return [random.randint(start,end) for _ in xrange(count)]

# nums = rand(0, 100, 1000)
# s.splitArray(nums, 50)
