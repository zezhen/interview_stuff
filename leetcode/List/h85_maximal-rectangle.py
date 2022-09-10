'''
https://leetcode.com/problems/maximal-rectangle/description/

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
'''

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # credit to https://leetcode.com/problems/maximal-rectangle/discuss/29054
        # very good explanation leetcode.com/problems/maximal-rectangle/discuss/29054/Share-my-DP-solution/175299
        # height[i] record the current number of countinous '1' in column i;
        # left[i] record the left most index j which satisfies that for any index k from j to  i, height[k] >= height[i];
        # right[i] record the right most index j which satifies that for any index k from i to  j, height[k] >= height[i];
        # by understanding the definition, we can easily figure out we need to update maxArea with value (height[i] * (right[i] - left[i] + 1));

        if not matrix: return 0

        col = len(matrix[0])
        height = [0] * col
        left = [0] * col
        right = [col] * col

        ans = 0
        for row in matrix:
            left_bound, right_bound = 0, col
            for j in xrange(col):
                height[j] = height[j] + 1 if row[j] == '1' else 0

            for j in xrange(col):
                if row[j] == '1':
                    left[j] = max(left[j], left_bound)
                else:
                    left[j] = 0
                    left_bound = j + 1

            for j in range(col)[::-1]:
                if row[j] == '1':
                    right[j] = min(right[j], right_bound)
                else:
                    right[j] = col
                    right_bound = j
            for j in range(col):
                ans = max(ans, height[j] * (right[j] - left[j]))

        return ans


s = Solution()
print s.maximalRectangle([["0"]]) == 0
print s.maximalRectangle([["1"]]) == 1
print s.maximalRectangle([["1","0","1","0","0"]]) == 1
print s.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]) == 6
print s.maximalRectangle([["0","0","0"],["0","0","0"],["1","1","1"]]) == 3