'''
https://leetcode.com/problems/daily-temperatures
https://leetcode.com/articles/daily-temperatures

Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature.  If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].


Note:
The length of temperatures will be in the range [1, 30000].
Each temperature will be an integer in the range [30, 100].
'''
from bisect import bisect_left
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        
        ans = [0] * len(T)
        
        queue = [- T[-1]] # negative to keep max abs(temperature) ahead
        index = [len(T) - 1]
        size = 1
        for i in xrange(len(T) - 2, -1, -1):
            j = bisect_left(queue, - T[i], 0, size)
            # print T[i], size, queue, j
            if j >= len(queue):
                queue.append(-T[i])
                index.append(i)
                size = len(queue)
            else:
                queue[j] = - T[i]
                index[j] = i
                size = j + 1

            if j > 0:
                ans[i] = index[j-1] - i

        return ans

s = Solution()
print s.dailyTemperatures([73]) == [0]
print s.dailyTemperatures([73,72]) == [0,0]
print s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
print s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
print s.dailyTemperatures([1,2,3,4,5,6,7,8]) == [1,1,1,1,1,1,1,0]
print s.dailyTemperatures([8,7,6,5,4,3,2,1]) == [0,0,0,0,0,0,0,0]
print s.dailyTemperatures([1,1,1,1,1,1,1,1]) == [0,0,0,0,0,0,0,0]
print s.dailyTemperatures([1,2,3,4,5,4,3,2,1]) == [1,1,1,1,0,0,0,0,0]
print s.dailyTemperatures([1,3,2,3,5,4,8,8,10]) == [1,3,1,1,2,1,2,1,0]
print s.dailyTemperatures(range(30000)) == [1]*29999 + [0]
print s.dailyTemperatures(range(30000,0,-1)) == [0]*30000
