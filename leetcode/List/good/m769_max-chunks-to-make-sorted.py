'''
https://leetcode.com/problems/max-chunks-to-make-sorted
https://leetcode.com/articles/max-chunks-to-make-sorted-i
Given an array arr that is a permutation of [0, 1, ..., arr.length - 1], we split the array into some number of "chunks" (partitions), and individually sort each chunk.  After concatenating them, the result equals the sorted array.

What is the most number of chunks we could have made?

Example 1:


Input: arr = [4,3,2,1,0]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.


Example 2:


Input: arr = [1,0,2,3,4]
Output: 4
Explanation:
We can split into two chunks, such as [1, 0], [2, 3, 4].
However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.


Note:


	arr will have length in range [1, 10].
	arr[i] will be a permutation of [0, 1, ..., arr.length - 1].


 
'''
class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        ans, s, e = 0, 0, -1

        while s < len(arr):
            # when start from a new group(e = -1)
            # the first element is in right position
            # create a new group
            if e == -1 and arr[s] == s:
                    ans += 1
                    s += 1
                    continue
            
            # s reach a new position
            # update e if necessary
            e = max(e, arr[s])
            
            # if s reach to group end
            # create a new group and start from end+1
            # reset e
            if s == e:
                ans += 1
                s = e + 1
                e = -1
                continue
            
            s += 1
        
        return ans