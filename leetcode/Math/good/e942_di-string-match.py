'''
https://leetcode.com/problems/di-string-match
https://leetcode.com/articles/di-string-match
Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.

Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:


	If S[i] == "I", then A[i] < A[i+1]
	If S[i] == "D", then A[i] > A[i+1]


 

Example 1:


Input: "IDID"
Output: [0,4,1,3,2]



Example 2:


Input: "III"
Output: [0,1,2,3]



Example 3:


Input: "DDI"
Output: [3,2,0,1]



 

Note:


	1 <= S.length <= 10000
	S only contains characters "I" or "D".
'''

class Solution(object):
    # We track high (h = N - 1) and low (l = 0) numbers within [0 ... N - 1]. When we encounter 'I', we insert the current low number and increase it. With 'D', we insert the current high number and decrease it. In the end, h == l, so we insert that last number to complete the premutation.
    def diStringMatch(self, S):
        ans = []
        l, h = 0, len(S)
        for i in xrange(len(S)+1):
            if i == len(S) or S[i] == 'I':
                ans.append(l)
                l += 1
            else:
                ans.append(h)
                h -= 1
        return ans


    def diStringMatch0(self, S):
        """
        :type S: str
        :rtype: List[int]
        """

        # credit to https://leetcode.com/problems/di-string-match/discuss/194904

        left = right = 0
        res = [0]
        for i in S:
            if i == "I":
                right += 1
                res.append(right)
            else:
                left -= 1
                res.append(left)
        return [i - left for i in res]


s = Solution()

S = 'IDID'; print s.diStringMatch(S), s.diStringMatch0(S)
S = 'III'; print s.diStringMatch(S), s.diStringMatch0(S)
S = 'DDDI'; print s.diStringMatch(S), s.diStringMatch0(S)