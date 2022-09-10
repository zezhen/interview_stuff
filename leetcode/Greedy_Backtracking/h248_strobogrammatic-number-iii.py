'''
https://leetcode.com/problems/strobogrammatic-number-iii

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to count the total strobogrammatic numbers that exist in the range of low <= num <= high.

Example:

Input: low = "50", high = "100"
Output: 3 
Explanation: 69, 88, and 96 are three strobogrammatic numbers.
Note:
Because the range might be a large number, the low and high numbers are represented as string.
'''

class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """

        self.cache = {}
        def findStrobogrammatic(n):
            if n == 0:
                return []
            
            if n == 1:
                return ['0','1','8']
            
            if n == 2:
                return ['11','69','88','96']
            
            if n in self.cache:
                return self.cache[n]
            
            d = {}
            l = []
            for x in findStrobogrammatic(n-2):
                l.append('1'+x+'1')
                l.append('6'+x+'9')
                l.append('9'+x+'6')
                l.append('8'+x+'8')
                if(n>3):
                    y = x[1:-1]
                    if y in d:
                        continue
                    d[y] = 1
                    l.append('10'+y+'01')
                    l.append('60'+y+'09')
                    l.append('90'+y+'06')
                    l.append('80'+y+'08')

            self.cache[n] = l
            return l

        l, h = len(low), len(high)
        if l > h: return 0

        ans = 0
        candidates = findStrobogrammatic(l)
        for c in candidates:
            if h > l and c >= low or h == l and low <= c <= high: 
                ans += 1

        for i in xrange(l+1, h):
            ans += len(findStrobogrammatic(i))
        if h > l:
            candidates = findStrobogrammatic(h)
            for c in candidates:
                if c <= high: ans += 1

        return ans

s = Solution()
print '50'>'100'
print s.strobogrammaticInRange('50', '100')
print s.strobogrammaticInRange('5', '6')