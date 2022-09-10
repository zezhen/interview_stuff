'''
https://leetcode.com/problems/strobogrammatic-number-ii

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

Example:

Input:  n = 2
Output: ["11","69","88","96"]
'''
class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 1: return ['0', '1', '8']

        _dict = {'6':'9','9':'6','0':'0','8':'8','1':'1'}

        l = n // 2
        ans = []
        def dfs(num, i, l, n):
            if i == l:
                stro = map(lambda t:_dict[t], reversed(num))
                if n % 2 == 1:
                    for x in ['0', '1', '8']:
                        ans.append(''.join(num + [x] + stro))
                else:
                    ans.append(''.join(num + stro))
                return

            for k in _dict.keys():
                if i == 0 and k == '0': continue
                num.append(k)
                dfs(num, i+1, l, n)
                num.pop()

        dfs([], 0, l, n)
        return ans

s = Solution()
print s.findStrobogrammatic(0)
print s.findStrobogrammatic(1) == ['0', '1', '8']
print s.findStrobogrammatic(2)
print s.findStrobogrammatic(3)
print s.findStrobogrammatic(4)