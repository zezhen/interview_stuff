'''
https://leetcode.com/problems/remove-boxes
https://leetcode.com/articles/remove-boxes
Given several boxes with different colors represented by different positive numbers. 
You may experience several rounds to remove boxes until there is no box left. Each time you can choose some continuous boxes with the same color (composed of k boxes, k >= 1), remove them and get k*k points.
Find the maximum points you can get.


Example 1:
Input: 

[1, 3, 2, 2, 2, 3, 4, 3, 1]

Output:

23

Explanation: 

[1, 3, 2, 2, 2, 3, 4, 3, 1] 
----> [1, 3, 3, 4, 3, 1] (3*3=9 points) 
----> [1, 3, 3, 3, 1] (1*1=1 points) 
----> [1, 1] (3*3=9 points) 
----> [] (2*2=4 points)



Note:
The number of boxes n would not exceed 100.

'''
class Solution(object):
    
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        '''
        credit to https://leetcode.com/problems/remove-boxes/discuss/101310

        1. self-contained subproblem

        let's say T(i, j) is the points we remove the boxes [i, j] inclusive. We want to remove box[i], but we find box[m] == box[i], so we'd better keep it, remove [i+1, m-1] first, so the problem will be box[i], and box[m, j], the result of T(m, j) also depends on how many box[i] before m, thus it's not self-contained subproblem, we need additional information to make it be. 

        2. T(i, j, k)

        k means how many boxes attached to index i and has same color with box[i]. Our original problem now becomes T(0, n - 1, 0), since there is no boxes attached to the left of the input array at the beginning.

        The termination conditions now will be:
        a. T(i, i - 1, k) = 0: no boxes so no points, and this is true for any k (you can interpret it as nowhere to attach the boxes).
        b. T(i, i, k) = (k + 1) * (k + 1): only one box left in the subarray but we've already got k boxes of the same color attached to its left, so the total number of boxes of the same color is (k + 1) and the maximum point is (k + 1) * (k + 1).

        The recurrence relation is as follows and the maximum points will be the larger of the two cases:
        a. If we remove boxes[i] first, we get (k + 1) * (k + 1) + T(i + 1, j, 0) points, where for the first term, instead of 1 we again get (k + 1) * (k + 1) points for removing boxes[i] due to the attached boxes to its left; and for the second term there will be no attached boxes so we have the 0 in this term.
        b. If we decide to attach boxes[i] to some other box of the same color, say boxes[m], then from our analyses above, the total points will be T(i + 1, m - 1, 0) + T(m, j, k + 1), where for the first term, since there is no attached boxes for subarray boxes[i + 1, m - 1], we have k = 0 for this part; while for the second term, the total number of attached boxes for subarray boxes[m, j] will increase by 1 because apart from the original k boxes, we have to account for boxes[i]now, so we have k + 1 for this term. But we are not done yet. What if there are multiple boxes of the same color as boxes[i] within subarray boxes[i + 1, j]? We have to try each of them and choose the one that yields the maximum points. Therefore the final answer for this case will be: max(T(i + 1, m - 1, 0) + T(m, j, k + 1)) where i < m <= j && boxes[i] == boxes[m].
        '''

        n = len(boxes)
        dp = [[[0] * n for _ in xrange(n)] for _ in xrange(n)]

        for i in xrange(n):
            for k in xrange(n):
                dp[i][i][k] = (k+1) * (k+1)

        for l in xrange(1, n):
            for i in xrange(n-l):
                j = i + l

                for k in xrange(i+1):
                    # dp[i][j][k]
                     dp[i][j][k] = (k+1) * (k+1) + dp[i+1][j][0]

                     for m in xrange(i+1, j+1):
                        if boxes[m] == boxes[i]:
                            dp[i][j][k] = max(dp[i][j][k], dp[i+1][m-1][0] + dp[m][j][k+1])

        return dp[0][n-1][0] if n > 0 else 0


    def removeBoxes_up_down(self, boxes):
        n = len(boxes)
        memo = {}
        def removeBoxesSub(i, j, k):
            if i > j: return 0
            if (i, j, k) in memo: return memo[(i,j,k)]

            while i + 1 <= j and boxes[i+1] == boxes[i]:
                i += 1
                k += 1
            res = removeBoxesSub(i + 1, j, 0) + (k+1)*(k+1)
            for m in xrange(i+1, j+1):
                if boxes[i] == boxes[m]:
                    res = max(res, removeBoxesSub(i+1, m-1, 0) + removeBoxesSub(m, j, k+1))

            memo[(i, j, k)] = res
            return res
        return removeBoxesSub(0, n-1, 0)



    memo = {}
    def removeBoxes_timeout(self, boxes):
        t = ''.join(map(str, boxes))
        if t in self.memo:
            return self.memo[t]

        ans = 0
        i = 0
        while i < len(boxes):
            # remove i
            j = i
            while j < len(boxes) -1 and boxes[j+1] == boxes[j]:
                j += 1
            ans = max(ans, (j-i+1) * (j-i+1) + self.removeBoxes(boxes[:i] + boxes[j+1:]))
            i = j + 1

        self.memo[t] = ans
        return ans

    def removeBoxes_dp_wrong(self, boxes):
        # dp[i][j] represent the points that remove boxes between [i,j]
        # dp[i][j] = max(dp[i][k], dp[k+1][j])
        # if boxes[x:k] and boxes[k+1,y] in same color, dp[i][j] = dp[i][j] - (k-x)^2 - (y-k-1)^2 + (y-x)^2
        # dp[0][n] is the answer

        # wrong: not work correctly on case 3, 2, 3, 2, 3

        n = len(boxes)
        dp = [[0] * n for _ in xrange(n)]

        for i in xrange(n):
            dp[i][i] = 1
        
        for l in xrange(1, n):
            for i in xrange(n-l):
                j = i + l
                for k in xrange(i, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k+1][j])
                    lo, hi = i, j
                    while lo < j and boxes[lo] == boxes[j]:
                        lo += 1
                    while hi > i and boxes[hi] == boxes[i]:
                        hi -= 1
                    if lo > i or j > hi:
                        if lo <= hi:
                            dp[i][j] = max(dp[i][j], dp[lo][hi] + (lo - i + j - hi)*(lo - i + j - hi))
                        else:
                            dp[i][j] = max(dp[i][j], (j-i+1)*(j-i+1))

        print dp
        return dp[0][n-1]

s = Solution()
print s.removeBoxes_up_down([1, 3, 2, 2, 2, 3, 4, 3, 1]) == 23
print s.removeBoxes_up_down([3, 8, 8, 5, 5, 3, 9, 2, 4, 4, 6, 5, 8, 4, 8, 6, 9, 6, 2, 8, 6, 4, 1, 9, 5, 3, 10, 5, 3, 3, 9, 8, 8, 6, 5, 3, 7, 4, 9, 6, 3, 9, 4, 3, 5, 10, 7, 6, 10, 7]) == 136
