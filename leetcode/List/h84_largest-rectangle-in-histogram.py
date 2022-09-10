'''
https://leetcode.com/problems/largest-rectangle-in-histogram/description/

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

https://assets.leetcode.com/uploads/2018/10/12/histogram.png


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

 
https://assets.leetcode.com/uploads/2018/10/12/histogram_area.png

The largest rectangle is shown in the shaded area, which has area = 10 unit.

 

Example:

Input: [2,1,5,6,2,3]
Output: 10

'''
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        n = len(heights)
        leftFirstLess = [0] * n
        rightFirstLess = [0] * n

        leftFirstLess[0] = -1
        rightFirstLess[-1] = n

        for i in xrange(1, n):
            p = i - 1
            while p >= 0 and heights[p] >= heights[i]:
                p = leftFirstLess[p]
            leftFirstLess[i] = p

        for i in range(n-1)[::-1]:
            p = i + 1
            while p < n and heights[p] >= heights[i]:
                p = rightFirstLess[p]
            rightFirstLess[i] = p

        ans = 0
        for i in xrange(n):
            ans = max(ans, heights[i] * (rightFirstLess[i] - leftFirstLess[i] - 1))

        return ans

    def largestRectangleArea2(self, heights):
        n, ans, stack = len(heights), 0, []
        i = 0
        while i <= n:
            h = heights[i] if i < n else 0
            if not stack or h >= heights[stack[-1]]:
                stack.append(i) # keep height[i] is increasing
                i += 1
            else:
                # calculate the area for height[j], index r is the exclusive right boundary
                # if stack is empty, that means all heights[k] > heights[j], thus pop out, width = i
                # otherwise index stack[-1] is the left boundary as heights[stack[-1]] <= heights[j]
                # height * width is the area. 
                # if heights[stack[-1]] == heights[j], as i keep as current, next round will check stack[-1]
                j = stack.pop() 
                width = i if not stack else (i - 1 - stack[-1])
                ans = max(ans, heights[j] * width)
        return ans


s = Solution()
print s.largestRectangleArea([1,2,3,4,5,6])
print s.largestRectangleArea2([1,2,3,4,5,6])