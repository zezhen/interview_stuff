'''
https://leetcode.com/problems/permutation-sequence
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:


	"123"
	"132"
	"213"
	"231"
	"312"
	"321"


Given n and k, return the kth permutation sequence.

Note:


	Given n will be between 1 and 9 inclusive.
	Given k will be between 1 and n! inclusive.


Example 1:


Input: n = 3, k = 3
Output: "213"


Example 2:


Input: n = 4, k = 9
Output: "2314"

'''
import operator
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = range(1, n+1)
        fact = [1]*(n)
        for i in range(1, n):
            fact[i] = fact[i-1]*nums[i-1]
        #print fact
        result = []
        k -= 1
        for i in range(1,n+1):
            index = k/fact[n-i]
            result.append(str(nums[index]))
            del nums[index]
            k = k%fact[n-i]
        return ''.join(result)

s = Solution()
print s.getPermutation(3,3)
print s.getPermutation(9,72)
        