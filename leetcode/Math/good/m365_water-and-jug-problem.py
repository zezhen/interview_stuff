'''
https://leetcode.com/problems/water-and-jug-problem

You are given two jugs with capacities x and y litres. There is an infinite amount of water supply available. You need to determine whether it is possible to measure exactly z litres using these two jugs.

If z liters of water is measurable, you must have z liters of water contained within one or both buckets by the end.

Operations allowed:


	Fill any of the jugs completely with water.
	Empty any of the jugs.
	Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.


Example 1: (From the famous "Die Hard" example)


Input: x = 3, y = 5, z = 4
Output: True


Example 2:


Input: x = 2, y = 6, z = 5
Output: False
'''

class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if z > (x + y): False
        if z == (x+y) or z % x == 0 or z % y == 0: return True

        def gcd(n, m):
            while m != 0:
                n, m = m, n % m
            return n


        

        return z % gcd(x, y) == 0

s = Solution()
for i in xrange(1,9):
    assert s.canMeasureWater(3,5,i) == True

assert s.canMeasureWater(3,5,7) == True

print s.canMeasureWater(2,6,4)
print s.canMeasureWater(2,6,5)
print s.canMeasureWater(3,10,8)
print s.canMeasureWater(31,52,8)