'''
https://leetcode.com/problems/trapping-rain-water/description/

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        left_max = [0] * len(height)
        right_max = [0] * len(height)

        for i in range(1, len(height)-1):
            left_max[i] = max(left_max[i-1], height[i-1])
        for i in range(1, len(height)-1)[::-1]:
            right_max[i] = max(right_max[i+1], height[i+1])

        print left_max
        print right_max

        ans = 0
        for i in range(1, len(height)-1):
            h = min(left_max[i], right_max[i])
            if h > height[i]:
                ans += (h - height[i])

        return ans

    def trap_faster(self, height):
        if not height or len(height) == 0:
            return 0

        l = level = water = 0
        r = len(height) - 1
        lower = None
        
        while l < r:
            if height[l] < height[r]:
                lower = height[l];
                l += 1
            else:
                lower = height[r];
                r -= 1
            if lower > level:
                level = lower
            water += level - lower
        return water


s = Solution()
print s.trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
print s.trap([0,1,0,2,1,0,1,1,1,1,1,1]) == 2
print s.trap([0,1,0,2,1,0,1,1,3,1,1,1]) == 6