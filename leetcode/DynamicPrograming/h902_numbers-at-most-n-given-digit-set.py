'''
https://leetcode.com/problems/numbers-at-most-n-given-digit-set/description/

We have a sorted set of digits D, a non-empty subset of {'1','2','3','4','5','6','7','8','9'}.  (Note that '0' is not included.)

Now, we write numbers using these digits, using each digit as many times as we want.  For example, if D = {'1','3','5'}, we may write numbers such as '13', '551', '1351315'.

Return the number of positive integers that can be written (using the digits of D) that are less than or equal to N.

 

Example 1:

Input: D = ["1","3","5","7"], N = 100
Output: 20
Explanation: 
The 20 numbers that can be written are:
1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.
Example 2:

Input: D = ["1","4","9"], N = 1000000000
Output: 29523
Explanation: 
We can write 3 one digit numbers, 9 two digit numbers, 27 three digit numbers,
81 four digit numbers, 243 five digit numbers, 729 six digit numbers,
2187 seven digit numbers, 6561 eight digit numbers, and 19683 nine digit numbers.
In total, this is 29523 integers that can be written using the digits of D.
 

Note:

D is a subset of digits '1'-'9' in sorted order.
1 <= N <= 10^9
'''
import bisect
class Solution(object):
    memo = {}
    def atMostNGivenDigitSet(self, D, N, drilldown=True):
        """
        :type D: List[str]
        :type N: int
        :rtype: int
        """
        if (N, drilldown) in self.memo:
            return self.memo[(N, drilldown)] 
        
        num = str(N)
        if len(num) <= 0: return 1
        
        ans = 0
        j = bisect.bisect_left(D, num[0])
        if j >= 0:
            ans += j * int(pow(len(D), len(num) - 1))
            print num, ans, j
            if j < len(D) and D[j] == num[0]:
                ans += self.atMostNGivenDigitSet(D, num[1:], False)
        if drilldown:
            for i in xrange(1, len(num)-1):
                ans += int(pow(len(D), i))
            
        print num, ans, j
        self.memo[(N,drilldown)] = ans
        return ans
        
    def atMostNGivenDigitSet(self, D, N):
        N = str(N)
        n = len(N)
        res = sum(len(D) ** i for i in range(1, n))
        i = 0
        while i < len(N):
            res += sum(c < N[i] for c in D) * (len(D) ** (n - i - 1))
            if N[i] not in D: break
            i += 1
        return res + (i == n)
        
        
s = Solution()
# print s.atMostNGivenDigitSet(["1","3","5","7"], 789)
print s.atMostNGivenDigitSet(["1","3","5","7"], 123)
print s.memo