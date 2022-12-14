'''
https://leetcode.com/problems/ugly-number-ii/description/

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:  

1 is typically treated as an ugly number.
n does not exceed 1690.

'''

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        primes = [2, 3, 5]
        index = [0 for i in range(len(primes))]
        uglyNums = [1]
        
        while len(uglyNums) < n:
            next = min(map(lambda (index,prime): uglyNums[index] * prime, zip(index, primes)))
            uglyNums.append(next)
            
            for i,prime in enumerate(primes):
                while uglyNums[index[i]] * prime <= next:
                    index[i] += 1
            
        return uglyNums[-1]

s = Solution()
print s.nthUglyNumber(5)