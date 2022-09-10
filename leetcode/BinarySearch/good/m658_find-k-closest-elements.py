'''
https://leetcode.com/problems/find-k-closest-elements/description/

Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]
Example 2:
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]
Note:
The value k is positive and will always be smaller than the length of the sorted array.
Length of the given array is positive and will not exceed 104
Absolute value of elements in the array and x will not exceed 104
UPDATE (2017/9/19):
The arr parameter had been changed to an array of integers (instead of a list of integers). Please reload the code definition to get the latest changes.
'''


# refer to https://leetcode.com/problems/find-k-closest-elements/discuss/106419
# find the left index rather than the k elements
'''
public List<Integer> findClosestElements(List<Integer> arr, int k, int x) {
    int lo = 0, hi = arr.size() - k;
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        if (x - arr.get(mid) > arr.get(mid+k) - x)
            lo = mid + 1;
        else
            hi = mid;
    }
    return arr.subList(lo, lo + k);
}
'''

import bisect

class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        i = bisect.bisect_left(arr, x)
        
        if i == 0: 
        	return arr[:k]
    	elif i == len(arr):
    		return arr[-k:]

    	k -= 1
    	start, end = i, i
    	while k > 0:
	    	l, r = max(0, start-k/2), min(len(arr)-1, end+k/2)
	    	gap1 = arr[i] - arr[l]
	    	gap2 = arr[r] - arr[i]
	    	if gap1 == gap2:
	    		start = l
	    		end = r
	    		k -= (r - l)
	    	elif gap1 < gap2:
	    		start = l
	    		k -= (i - l)
	    	else:
	    		end = r
	    		k -= (r - i)


        return arr[start:end]
        