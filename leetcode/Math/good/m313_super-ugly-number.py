'''
https://leetcode.com/problems/super-ugly-number
Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k.

Example:


Input: n = 12, primes = [2,7,13,19]
Output: 32 
Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 
             super ugly numbers given primes = [2,7,13,19] of size 4.

Note:


	1 is a super ugly number for any given primes.
	The given numbers in primes are in ascending order.
	0 < k <= 100, 0 < n <= 106, 0 < primes[i] < 1000.
	The nth super ugly number is guaranteed to fit in a 32-bit signed integer.

'''
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        if n == 1:
            return 1

        index = [0 for i in range(len(primes))]
        uglyNums = [1]
        
        while len(uglyNums) < n:
            next = min(map(lambda (index,prime): uglyNums[index] * prime, zip(index, primes)))
            uglyNums.append(next)
            
            for i,prime in enumerate(primes):
                while uglyNums[index[i]] * prime <= next:
                    index[i] += 1
            
        return uglyNums[-1]
            

