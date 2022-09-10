'''
https://leetcode.com/problems/remove-k-digits
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.


Note:

The length of num is less than 10002 and will be >= k.
The given num does not contain any leading zero.




Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.



Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.



Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.

'''

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """

        # wrong coding, need to handle corner cases

        def strip0(n):
            i = 0
            while i < len(n) and n[i] == '0': i += 1
            if i == len(n): return '0'
            return n[i:]

        if k >= len(num): return '0'
        if k == 0: return num
        
        ans = []
        for i in xrange(len(num)-1):
            # print i, ans
            if num[i] <= num[i+1]:
                ans.append(num[i])
            else:
                k -= 1
                if k == 0: break
        else:
            print k
            # from tail remove that
            return strip0(''.join(ans[:len(ans)-k+1]))
        
        return strip0(''.join(ans) + num[i+1:])

s = Solution()
# print s.removeKdigits('10', 2)
# print s.removeKdigits('1432219', 3)
# print s.removeKdigits('10200', 1)
# print s.removeKdigits('1234567', 3)
# print s.removeKdigits('7654321', 3)
# print s.removeKdigits('10', 1)
print s.removeKdigits("1234567890", 9)
