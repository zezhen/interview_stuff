'''
https://leetcode.com/problems/super-palindromes/description/

Let's say a positive integer is a superpalindrome if it is a palindrome, and it is also the square of a palindrome.

Now, given two positive integers L and R (represented as strings), return the number of superpalindromes in the inclusive range [L, R].

 

Example 1:

Input: L = "4", R = "1000"
Output: 4
Explanation: 4, 9, 121, and 484 are superpalindromes.
Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.
 

Note:

1 <= len(L) <= 18
1 <= len(R) <= 18
L and R are strings representing integers in the range [1, 10^18).
int(L) <= int(R)
 
'''
import math
class Solution(object):
    def superpalindromesInRange(self, L, R):
        """
        :type L: str
        :type R: str
        :rtype: int
        """
        palindromes = set()

        def isPalindrome(n):
            if n < 10 or n in palindromes: return True

            s = str(n)
            size = len(s)
            for i in xrange(size // 2+1):
                if s[i] != s[size-1-i]: return False
            else:
                palindromes.add(n)
                return True
        
        ans = 0
        start = int(math.sqrt(int(L)))
        end = int(math.sqrt(int(R))) + 1
        for i in xrange(start, end+1):
            if i*i > int(R): break
            if isPalindrome(i) and isPalindrome(i*i): 
                # print i, i*i
                ans += 1
        return ans

s = Solution()
# print s.superpalindromesInRange(10000,100000000)
print s.superpalindromesInRange("96915129", "1492347521772") # time exceed