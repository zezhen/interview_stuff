'''
https://leetcode.com/problems/russian-doll-envelopes/description/

You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Note:
Rotation is not allowed.

Example:

Input: [[5,4],[6,4],[6,7],[2,3]]
Output: 3 
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
'''

class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """


'''
I cannot come out with a solution

optimal solution:
1. Sort the array. Ascend on width and descend on height if width are same.
	Since the width is increasing, we only need to consider height.
	[3, 4] cannot contains [3, 3], so we need to put [3, 4] before [3, 3] when sorting otherwise it will be counted as an increasing number if the order is [3, 3], [3, 4]
2. Find the longest increasing subsequence based on height.

# public int maxEnvelopes(int[][] envelopes) {
#     if(envelopes == null || envelopes.length == 0 
#        || envelopes[0] == null || envelopes[0].length != 2)
#         return 0;
#     Arrays.sort(envelopes, new Comparator<int[]>(){
#         public int compare(int[] arr1, int[] arr2){
#             if(arr1[0] == arr2[0])
#                 return arr2[1] - arr1[1];
#             else
#                 return arr1[0] - arr2[0];
#        } 
#     });
#     int dp[] = new int[envelopes.length];
#     int len = 0;
#     for(int[] envelope : envelopes){
#         int index = Arrays.binarySearch(dp, 0, len, envelope[1]);
#         if(index < 0)
#             index = -(index + 1);
#         dp[index] = envelope[1];
#         if(index == len)
#             len++;
#     }
#     return len;
# }


'''        