'''
https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size

Given an integer array sorted in ascending order, write a function to search target in nums.  If target exists, then return its index, otherwise return -1. However, the array size is unknown to you. You may only access the array using an ArrayReader interface, where ArrayReader.get(k) returns the element of the array at index k (0-indexed).

You may assume all integers in the array are less than 10000, and if you access the array out of bounds, ArrayReader.get will return 2147483647.

 

Example 1:

Input: array = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: array = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Note:

You may assume that all elements in the array are unique.
The value of each element in the array will be in the range [-9999, 9999].
'''

class Solution(object):
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        x = reader.get(0)
        if x > target: return -1

        e = 1
        while reader.get(e) < target:
        	e *= 2

        s = e / 2
        if reader.get(s) == target: return s

        while s <= e:
        	m = s + ((e - s) >> 1)
        	x = reader.get(m)
        	if x == target: 
        		return m
        	elif x > target:
        		e = m - 1
        	else:
        		s = m + 1

        return -1


class ArrayReader:
	def __init__(self, array):
		self.array = array

	def get(self, k):
		if k < 0 or k >= len(self.array): return 2147483647
		return self.array[k]
class RangeReader:
	def __init__(self, n):
		self.n = n
	def get(self, k):
		if k < 0 or k >= self.n: return 2147483647
		return k

array = [-1,0,3,5,9,12]
reader = ArrayReader(array)
s = Solution()

assert s.search(reader, -2) == -1
assert s.search(reader, -1) == 0
assert s.search(reader, 0) == 1
assert s.search(reader, 3) == 2
assert s.search(reader, 5) == 3
assert s.search(reader, 9) == 4
assert s.search(reader, 12) == 5
assert s.search(reader, 13) == -1

reader = ArrayReader(range(100))
assert s.search(reader, 128) == -1
assert s.search(reader, 99) == 99

reader = ArrayReader(range(1025))
assert s.search(reader, 1026) == -1


reader = RangeReader(10**9)
assert s.search(reader, 10**8) == 10**8
