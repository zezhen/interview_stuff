'''
https://leetcode.com/problems/maximum-swap
https://leetcode.com/articles/maximum-swap

Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.


Example 1:

Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.



Example 2:

Input: 9973
Output: 9973
Explanation: No swap.




Note:

The given number is in the range [0, 108]

'''
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = self.to_digits(num)
        
        # right_max[i] keep the index of max number after i (inclusive)
        right_max = [0] * len(digits)
        right_max[-1] = -1 # index
        for i in xrange(1, len(digits)):
            max_i = right_max[-i]
            if digits[max_i] < digits[-1-i]:
                right_max[-1-i] = -1-i
            else:
                right_max[-1-i] = max_i
        
        # find the first digit that has a larger number at right
        # choose the last one if it has duplicated numbers
        for i in xrange(len(digits)):
            max_i = right_max[i]
            if digits[i] < digits[max_i]:
                digits[i], digits[max_i] = digits[max_i], digits[i]
                break
        
        return self.to_number(digits)

    def to_number(self, digits):
        ans, multiply = 0, 1
        for i in xrange(len(digits)):
            ans += digits[-1-i] * multiply
            multiply *= 10
        return ans
    
    def to_digits(self, num):
        ans = []
        while num > 0:
            m = num % 10
            ans.append(m)
            num /= 10
        return ans[::-1]