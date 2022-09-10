'''
https://leetcode.com/problems/integer-replacement

Given a positive integer n and you can do operations as follow:




If n is even, replace n with n/2.
If n is odd, you can replace n with either n + 1 or n - 1.




What is the minimum number of replacements needed for n to become 1?




Example 1:

Input:
8

Output:
3

Explanation:
8 -> 4 -> 2 -> 1



Example 2:

Input:
7

Output:
4

Explanation:
7 -> 8 -> 4 -> 2 -> 1
or
7 -> 6 -> 3 -> 2 -> 1

'''
class Solution(object):
    def integerReplacement_bit(self, n):
        count = 0
        while n > 1:

            count += 1
            if n & 1 == 0:
                n >>= 1
            else:
                if n > 3 and bin(n)[-2] == '1':
                    n = n + 1
                else: 
                    n = n - 1
        return count

    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {}
        def operation(x):
            if x == 1: return 0
            if x in memo: return memo[x]

            if x % 2 == 0:
                count = operation(x//2)+1
            else:
                count = 1 + min(operation(x+1), operation(x-1))

            memo[x] = count
            return count

        return operation(n)

s = Solution()
print s.integerReplacement(8) == 3
print s.integerReplacement(7) == 4
print s.integerReplacement(100000000)