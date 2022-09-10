'''
https://leetcode.com/problems/range-sum-query-mutable
https://leetcode.com/articles/range-sum-query-mutable
Given an integer array nums, find the sum of the elements between indices i and j (i <= j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.

Example:


Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8


Note:


	The array is only modifiable by the update function.
	You may assume the number of calls to update and sumRange function is distributed evenly.

'''

import math
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.N = int(math.pow(2, math.ceil(math.log(len(nums), 2))))
        self.tree = [0] * (2*self.N)
        

        for i in xrange(len(nums)):
            self.tree[self.N+i] = nums[i]

        for i in xrange(self.N-1,0,-1):
            self.tree[i] = self.tree[i * 2] + self.tree[i*2+1]
        

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.tree[i+self.N] = val
        i += self.N

        while i > 1:
            self.tree[i // 2] = self.tree[i] + self.tree[i^1]
            i //= 2

    def _sum_helper(self, start, end, node, node_start, node_end):
        if start == node_start and end == node_end:
            return self.tree[node]
        mid = (node_start + node_end) // 2
        if end <= mid:
            return self._sum_helper(start, end, 2 * node, node_start, mid)
        else:
            if mid + 1 <= start:
                return self._sum_helper(start, end, 2 * node + 1, mid + 1, node_end)
            else:
                return self._sum_helper(start, mid, 2 * node, node_start, mid) + \
                    self._sum_helper(mid + 1, end, 2 * node + 1, mid + 1, node_end)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self._sum_helper(i, j, 1, 0, self.N - 1)



if __name__ == '__main__':
    nums = range(1,13)
    tree = NumArray(nums)

    def verify():
        for i in xrange(len(nums)):
            for j in xrange(i, len(nums)):
                assert tree.sumRange(i, j) == sum(nums[i:j+1])

    verify()
    tree.update(5, 10)
    nums[5] = 10
    verify()

    # https://github.com/openai/baselines/blob/master/baselines/common/segment_tree.py