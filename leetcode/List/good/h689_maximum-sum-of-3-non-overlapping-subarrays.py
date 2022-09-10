'''
https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/description/

In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.

Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.

Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

Example:
Input: [1,2,1,2,6,7,5,1], 2
Output: [0, 3, 5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
Note:
nums.length will be between 1 and 20000.
nums[i] will be between 1 and 65535.
k will be between 1 and floor(nums.length / 3).

'''

class Solution(object):
    # the logic is a bit complicated, I forgot how it come from after 2 months
    # refer to below java solution
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        length = len(nums)
        if length < 3 * k: assert False

        # dp[n][m] means find m non-overlap subarrys(length=k) within a n length array
        # if n < k*m, dp[n][m] = 0
        # elif n == k*m, dp[n][m] = sum(arr[:n])
        # else we need to consider whether the last number is included or not
        #   dp[n][m] = max(dp[n-1][m], dp[n-k][m-1] + sum(nums[n-k:n]))
        dp = [[0,0,0,0] for _ in range(len(nums)+1)]
        # direction = 1 means keep current number, other skip it
        direction = [[0,0,0,0] for _ in range(len(nums)+1)]
        
        acc = [0] * length
        acc[0] = nums[0]
        for i in range(1, length):
            acc[i] = acc[i-1] + nums[i]
        
        
        for i in range(k, length+1):
            for j in range(1,4):
                if i < j*k: break
                if i == j * k:
                    dp[i][j] = acc[i-1]
                    direction[i][j] = 1
                else:
                    a = dp[i-1][j]
                    b = dp[i-k][j-1] + acc[i-1] - acc[i-k-1]
                    if a >= b:
                        dp[i][j] = a
                        direction[i][j] = 0
                    else:
                        dp[i][j] = b
                        direction[i][j] = 1
        
        # look back from direction[n][3]
        n, count = length, 3
        ans = [0] * count

        while count > 0:
            while direction[n][count] == 0:
                n -= 1
            n -= k
            count -= 1
            ans[count] = n
        
        return ans


# credit to https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/discuss/108231
'''
class Solution {
    public int[] maxSumOfThreeSubarrays(int[] nums, int k) {
        int n = nums.length, maxsum = 0;
        int[] sum = new int[n+1], posLeft = new int[n], posRight = new int[n], ans = new int[3];
        for (int i = 0; i < n; i++) sum[i+1] = sum[i]+nums[i];
        // DP for starting index of the left max sum interval
        for (int i = k, tot = sum[k]-sum[0]; i < n; i++) {
            if (sum[i+1]-sum[i+1-k] > tot) {
                posLeft[i] = i+1-k;
                tot = sum[i+1]-sum[i+1-k];
            }
            else
                posLeft[i] = posLeft[i-1];
        }
        // DP for starting index of the right max sum interval
       // caution: the condition is ">= tot" for right interval, and "> tot" for left interval
        posRight[n-k] = n-k;
        for (int i = n-k-1, tot = sum[n]-sum[n-k]; i >= 0; i--) {
            if (sum[i+k]-sum[i] >= tot) {
                posRight[i] = i;
                tot = sum[i+k]-sum[i];
            }
            else
                posRight[i] = posRight[i+1];
        }
        // test all possible middle interval
        for (int i = k; i <= n-2*k; i++) {
            int l = posLeft[i-1], r = posRight[i+k];
            int tot = (sum[i+k]-sum[i]) + (sum[l+k]-sum[l]) + (sum[r+k]-sum[r]);
            if (tot > maxsum) {
                maxsum = tot;
                ans[0] = l; ans[1] = i; ans[2] = r;
            }
        }
        return ans;
    }
}
'''