'''
https://leetcode.com/problems/k-similar-strings
https://leetcode.com/articles/k-similar-strings
Strings A and B are K-similar (for some non-negative integer K) if we can swap the positions of two letters in A exactly K times so that the resulting string equals B.

Given two anagrams A and B, return the smallest K for which A and B are K-similar.

Example 1:


Input: A = "ab", B = "ba"
Output: 1



Example 2:


Input: A = "abc", B = "bca"
Output: 2



Example 3:


Input: A = "abac", B = "baca"
Output: 2



Example 4:


Input: A = "aabc", B = "abca"
Output: 2




Note:


	1 <= A.length == B.length <= 20
	A and B contain only lowercase letters from the set {'a', 'b', 'c', 'd', 'e', 'f'}

'''
class Solution(object):
    def kSimilarity_bfs(self, A, B):
        # greedy only switch with the nearest one
        # bfs need to switch with all possiblilities
        pass



    def kSimilarity_greedy(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        assert len(A) == len(B), 'length A and B should be equal'
        A = [c for c in A]
        B = [c for c in B]

        i = ans =0
        while True:
            while i < len(A) and A[i] == B[i]:
                i += 1

            if i == len(A):
                return ans

            for k in xrange(i+1, len(A)):
                if A[k] == B[i]: break

            A[k], A[i] = A[i], A[k]
            ans += 1

            i += 1
        
        return ans


s = Solution()

assert s.kSimilarity("ba", "ba") == 0
assert s.kSimilarity("ba", "ab") == 1
assert s.kSimilarity("abc", "bca") == 2
assert s.kSimilarity("abac", "baca") == 2
assert s.kSimilarity("aabc", "abca") == 2

"bcaacacceecdeea"
"bcaacceeccdeaae"
