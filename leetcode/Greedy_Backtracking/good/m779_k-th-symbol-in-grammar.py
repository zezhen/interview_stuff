'''
https://leetcode.com/problems/k-th-symbol-in-grammar
https://leetcode.com/articles/k-th-symbol-in-grammar
On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

Given row N and index K, return the K-th indexed symbol in row N. (The values of K are 1-indexed.) (1 indexed).


Examples:
Input: N = 1, K = 1
Output: 0

Input: N = 2, K = 1
Output: 0

Input: N = 2, K = 2
Output: 1

Input: N = 4, K = 5
Output: 1

Explanation:
row 1: 0
row 2: 01
row 3: 0110
row 4: 01101001


Note:


	N will be an integer in the range [1, 30].
	K will be an integer in the range [1, 2^(N-1)].

'''
import math
class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        # row i has 2^(i-1) elements
        # the first 2^(i-2) elements in row i is same as 
        # all elements in row (i-1)
        reverse = False
        while K > 2:
            x = int(math.pow(2, N-2))
            if K > x:
                K -= x
                reverse ^= True
            else:
                N -= 1

        ans = 0 if K == 1 else 1
        return ans ^ (1 if reverse else 0)

s = Solution()
print s.kthGrammar(1, 1) == 0
print s.kthGrammar(2, 1) == 0
print s.kthGrammar(2, 2) == 1
print s.kthGrammar(3, 1) == 0
print s.kthGrammar(3, 2) == 1
print s.kthGrammar(3, 3) == 1
print s.kthGrammar(3, 4) == 0
print s.kthGrammar(4, 2) == 1
print s.kthGrammar(4, 3) == 1
print s.kthGrammar(4, 4) == 0
print s.kthGrammar(4, 5) == 1
print s.kthGrammar(4, 6) == 0
print s.kthGrammar(4, 7) == 0
print s.kthGrammar(4, 8) == 1