'''
https://leetcode.com/problems/counting-bits
https://leetcode.com/articles/counting-bits
Given a non negative integer number num. For every numbers i in the range 0 <= i <= num calculate the number of 1's in their binary representation and return them as an array.

Example 1:


Input: 2
Output: [0,1,1]

Example 2:


Input: 5
Output: [0,1,1,2,1,2]


Follow up:


	It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
	Space complexity should be O(n).
	Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
'''

class Solution(object):
    # the difference between countBits and countBit1 is the implementation
    # the former is more clear and efficient, it contain less check conditions.
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        bits = [0] * (num+1)
        if num == 0: return bits

        bits[1] = 1
        i, lookback, times = 2, 2, 0
        while i <= num:
            bits[i] = bits[i-lookback] + 1
            i += 1
            times += 1
            if times == lookback:
                times = 0
                lookback *= 2
        return bits


    def countBits1(self, num):
        if num == 0:
            return [0]
        elif num == 1:
            return [0, 1]
        
        ret = [0] * (num + 1)
        ret[1] = 1
        
        base = 2
        done = False
        while not done:
            for i in range(base):
                if base+i > num:
                    done = True
                    break
                ret[base+i] = 1 + ret[i]
            base *= 2
        return ret

s = Solution()

num = 1000000
assert s.countBits1(num) == s.countBits(num)