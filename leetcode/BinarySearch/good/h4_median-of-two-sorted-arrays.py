'''
https://leetcode.com/problems/median-of-two-sorted-arrays/description/

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """


        # refer to https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2481

        # we need find a split i for A and j for B that
        # 1. i + j (left part) == m - i + n - j (or m - i + n - j + 1)  (right part)
        #     => assume n >= m, search i in [0,m], j = (m+n+1) / 2 - i
        #     => if m >= n, switch A and B, to make sure j >= 0
        # 2. B[j-1] <= A[i] and A[i-1] <= B[j] (left part <= right part)

        # so the problem is to find the right i, meets above two conditions.

        # boundary scenarios:
        #  i == 0: the max of left is B[j-1]
        #  j == 0: the max of left is A[i-1]
        #  i == m: the min of right is B[j]
        #  j == n: the min of right is A[i]

        # if m+n is odd: return max of left
        # else return average of max of left + min of right


        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) / 2
        while imin <= imax:
            i = (imin + imax) / 2
            j = half_len - i
            if i < m and B[j-1] > A[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and A[i-1] > B[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect

                if i == 0: max_of_left = B[j-1]
                elif j == 0: max_of_left = A[i-1]
                else: max_of_left = max(A[i-1], B[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m: min_of_right = B[j]
                elif j == n: min_of_right = A[i]
                else: min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0