'''
https://leetcode.com/problems/max-chunks-to-make-sorted-ii
https://leetcode.com/articles/max-chunks-to-make-sorted-ii
This question is the same as "Max Chunks to Make Sorted" except the integers of the given array are not necessarily distinct, the input array could be up to length 2000, and the elements could be up to 10**8.



Given an array arr of integers (not necessarily distinct), we split the array into some number of "chunks" (partitions), and individually sort each chunk.  After concatenating them, the result equals the sorted array.

What is the most number of chunks we could have made?

Example 1:


Input: arr = [5,4,3,2,1]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3], which isn't sorted.


Example 2:


Input: arr = [2,1,3,4,4]
Output: 4
Explanation:
We can split into two chunks, such as [2, 1], [3, 4, 4].
However, splitting into [2, 1], [3], [4], [4] is the highest number of chunks possible.


Note:


	arr will have length in range [1, 2000].
	arr[i] will be an integer in range [0, 10**8].


 
'''
class Solution(object):
    def maxChunksToSorted_faster(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        min_right = [float('inf')] * len(arr)
        for i in range(len(arr)-2, -1, -1):
            min_right[i] = min(min_right[i+1], arr[i+1])
        res = 0
        curr_max = float('-inf')
        for i, n in enumerate(arr):
            curr_max = max(curr_max, n)
            if curr_max <= min_right[i]:
                res += 1
        return res
    def maxChunksToSorted(self, arr):
        # create two array lmax and rmin
        # lmax[i] = max(arr[0:i-1])
        # rmin[i] = min(arr[i+1:])
        lmax, rmin = [0]*len(arr), [0]*len(arr)
        lmax[0] = -1
        for i in range(1, len(arr)):
            lmax[i] = max(lmax[i-1], arr[i-1])

        rmin[-1] = 10**8+1
        for i in range(len(arr)-2, -1, -1):
            rmin[i] = min(rmin[i+1], arr[i+1])

        s, ans = 0, 0
        while s < len(arr):
            # new group when max(arr[1:s-1]) <= arr[s] <= min(arr[s+1:])
            if lmax[s] <= arr[s] <= rmin[s]:
                ans += 1
                s += 1
                continue
            
            # new group if max(arr[1:s-1]) <= min(arr[s:e]) <= max(arr[s:e]) <= min(arr[e+1:])
            e = s + 1
            v_min = arr[s]
            v_max = arr[s]
            while True:
                if e >= len(arr): 
                    ans += 1
                    s = e + 1
                    break

                v_min = min(v_min, arr[e])
                v_max = max(v_max, arr[e])
                
                if lmax[s] <= v_min <= v_max <= rmin[e]:
                    ans += 1
                    s = e + 1
                    break

                e += 1

        return ans