'''
https://leetcode.com/problems/super-pow
Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

Example 1:



Input: a = 2, b = [3]
Output: 8



Example 2:


Input: a = 2, b = [1,0]
Output: 1024


'''
import math
class Solution(object):

    # better solution refer to https://leetcode.com/problems/super-pow/discuss/84472/
    # main idea is a^1234567 % k = (a^1234560 % k) * (a^7 % k) % k = (a^123456 % k)^10 % k * (a^7 % k) % k

    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        powR, n = 1, len(b) - 1
        mod = 1337
        
        a %= mod
        for i, e in enumerate(b):
            powR = (self._mod(powR, 10, mod) * self._mod(a, e, mod)) % mod
            
        return int(powR)
    
    def _mod(self, x, y, mod):
        n, ys = 5, []
        
        while y >= n:
            ys.append(n)
            y -= n
        if y > 0:
            ys.append(y)

        product = 1
        for y in ys:
            product *= math.pow(x, y) % mod
            product %= mod
        return product
        