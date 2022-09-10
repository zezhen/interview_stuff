'''
https://leetcode.com/problems/advantage-shuffle
https://leetcode.com/articles/advantage-shuffle
Given two arrays A and B of equal size, the advantage of A with respect to B is the number of indices i for which A[i] > B[i].

Return any permutation of A that maximizes its advantage with respect to B.

 


Example 1:


Input: A = [2,7,11,15], B = [1,10,4,11]
Output: [2,11,7,15]



Example 2:


Input: A = [12,24,8,32], B = [13,25,32,11]
Output: [24,32,8,12]


 

Note:


	1 <= A.length = B.length <= 10000
	0 <= A[i] <= 10^9
	0 <= B[i] <= 10^9



'''

class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        A.sort()
        Bp = zip(B, range(len(B)))
        Bp.sort(reverse=True)
        
        ans = [0] * len(A)

        high, low = len(A) - 1, 0
        for value, index in Bp:
            if A[high] > value:
                ans[index] = A[high]
                high -= 1
            else:
                ans[index] = A[low]
                low += 1

        return ans


s = Solution()
print s.advantageCount([2,7,11,15], [1,10,4,11]) == [2,11,7,15]
print s.advantageCount([12,24,8,32], [13,25,32,11]) == [24,32,8,12]
