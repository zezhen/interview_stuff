'''
https://leetcode.com/problems/monotone-increasing-digits
https://leetcode.com/articles/monotone-increasing-digits

Given a non-negative integer N, find the largest number that is less than or equal to N with monotone increasing digits.

(Recall that an integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.)


Example 1:

Input: N = 10
Output: 9



Example 2:

Input: N = 1234
Output: 1234



Example 3:

Input: N = 332
Output: 299



Note:
N is an integer in the range [0, 10^9].
'''
class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        
        digits = list(str(N))
        i = 0
        while i < len(digits) - 1:
            if digits[i] <= digits[i+1]:
                i += 1
            else:
                digits[i] = str(int(digits[i]) - 1)
                while i > 0 and digits[i] < digits[i-1]:
                    digits[i-1] = digits[i]
                    i -= 1
                break

        if i == len(digits) - 1:
            return N
        else:
            j = 1 if i == 0 and digits[i] == '0' else 0
            return int("".join(digits[j:i+1]) + '9' * (len(digits)-i-1))

s = Solution()
print s.monotoneIncreasingDigits(0) == 0
print s.monotoneIncreasingDigits(9) == 9
print s.monotoneIncreasingDigits(10) == 9
print s.monotoneIncreasingDigits(11) == 11
print s.monotoneIncreasingDigits(1234) == 1234
print s.monotoneIncreasingDigits(1232) == 1229
print s.monotoneIncreasingDigits(110) == 99
print s.monotoneIncreasingDigits(332) == 299
print s.monotoneIncreasingDigits(4321) == 3999
print s.monotoneIncreasingDigits(123421899) == 123399999
print s.monotoneIncreasingDigits(1111000) == 999999