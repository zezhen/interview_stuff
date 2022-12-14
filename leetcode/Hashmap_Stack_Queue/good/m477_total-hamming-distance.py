'''
https://leetcode.com/problems/total-hamming-distance
https://leetcode.com/articles/total-hamming-distance
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Now your job is to find the total Hamming distance between all pairs of the given numbers.


Example:

Input: 4, 14, 2

Output: 6

Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case). So the answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.



Note:

Elements of the given array are in the range of 0  to 10^9
Length of the array will not exceed 10^4. 

'''
class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # 1. xor on all pair, then count the numbers of 1, sum of count is the ans. O(n^2)
        # 2. 10^9 close to 2^30, so allocate 30 size bits array, and scan all numbers 
        #    and inc 1 if the bit is 1
        #    ans = sum(map(lambda v: v * (len(nums)-v), bits))