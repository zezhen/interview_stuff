# -*- coding: utf-8 -*-

'''
往一个int  array   代表海拔的格子里倒水，打印出倒水后的图， 输入：int[]   海拔， int 水数量， int    
倒得位置。
Example:
int[]   海拔 {5,4,2,1,2,3,2,1,0,1,2,4}
+
++        +
++  +     ++
+++ +++   ++
++++++++ +++
++++++++++++
012345678901
水数量8， 倒在位置5 ->
+
++        +
++www+    ++
+++w+++www++
++++++++w+++
++++++++++++
012345678901
'''

# need some assumption before go
# 1. water is 1 unit, cannot split into smaller
# 2. if water can go to left or right, we prefer to go left first

def pour_water(heights, water, location):
    
    if water <= 0 or location < 0 or location >= len(heights):
        return heights

    waters = [0] * len(heights)
    while water > 0:
        # check left first
        left = location - 1
        while left > 0:
            if heights[left] + waters[left] > heights[left + 1] + waters[left + 1]:
                break
            left -= 1
        leftPourLoc = left + 1
        # if heights[leftPourLoc] + waters[leftPourLoc] <= heights[leftPourLoc - 1] + waters[leftPourLoc - 1]:
        #     water -= 1
        #     waters[leftPourLoc] += 1

        # check right
        right = location + 1
        while right < len(heights) - 1:
            if heights[right] + waters[right] > heights[right - 1] + waters[right - 1]:
                break
            right += 1
        rightPourLoc = right - 1

        # if heights[rightPourLoc] + waters[rightPourLoc] <= heights[rightPourLoc + 1] + waters[rightPourLoc + 1]:
        #    water -= 1
        #    waters[rightPourLoc] += 1

        # here we always choose a lower position to add water
        # if we assume left has higher priority, then recomment above two commented block
        pourLoc = leftPourLoc if heights[leftPourLoc] <= heights[rightPourLoc] else rightPourLoc
        water -= 1
        waters[pourLoc] += 1

        print location, left, pourLoc, water, waters, heights
        

    print waters

pour_water([6,5,3,2,4,3,3,2,1,2,5,4], 10, 5)