'''
https://leetcode.com/problems/count-primes
Count the number of prime numbers less than a non-negative number, n.

Example:


Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
'''
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        elif n == 3:
            return 1
        elif n == 4:
            return 2
        
        count = 2
        
        # separate numbers into 6 groups, 6k+0, 6k+1, 6k+2, 6k+3, 6k+4, 6k+5
        # 6k+0, 6k+2, 6k+4 are divided by 2
        # 6k + 3 is divided by 3
        for i in xrange(5, n, 6):
            if self.is_prime(i):
                count += 1
        for i in xrange(7, n, 6):
            if self.is_prime(i):
                count += 1
                
        return count
    
    def is_prime(self, n):
        # Corner cases
        if n <= 1:
            return False
        if n <= 3:
            return True

        # (6k + 0), (6k + 2), (6k + 4) and
        # (6k + 3)
        if n%2 == 0 or n%3 == 0:
            return False

        for i in xrange(5, n, 6):
            if i*i > n: break
            if n%i == 0 or n%(i+2) == 0:
               return False

        return True