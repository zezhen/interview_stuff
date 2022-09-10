'''
https://leetcode.com/problems/partition-to-k-equal-sum-subsets/description/

Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:
Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Note:

1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.
'''

class Solution(object):


'''
    # https://leetcode.com/problems/partition-to-k-equal-sum-subsets/discuss/108730/JavaC++Straightforward-dfs-solution
    public boolean canPartitionKSubsets(int[] nums, int k) {
        int sum = 0;
        for(int num:nums)sum += num;
        if(k <= 0 || sum%k != 0)return false;
        int[] visited = new int[nums.length];
        return canPartition(nums, visited, 0, k, 0, 0, sum/k);
    }
    
    public boolean canPartition(int[] nums, int[] visited, int start_index, int k, int cur_sum, int cur_num, int target){
        if(k==1)return true;
        if(cur_sum == target && cur_num>0)return canPartition(nums, visited, 0, k-1, 0, 0, target);
        for(int i = start_index; i<nums.length; i++){
            if(visited[i] == 0){
                visited[i] = 1;
                if(canPartition(nums, visited, i+1, k, cur_sum + nums[i], cur_num++, target))return true;
                visited[i] = 0;
            }
        }
        return false;
    }

'''

    def canPartitionKSubsets(self, nums, k):
        # https://leetcode.com/problems/partition-to-k-equal-sum-subsets/discuss/146579/Easy-python-28-ms-beats-99.5
        if sum(nums) % k != 0: return False

        buckets = [0]*k
        target = sum(nums) / k
        nums.sort(reverse=True) # starting with bigger ones makes it faster
        l = len(nums)
        
        def walk(i):
            if i == l:
                return len(set(buckets)) == 1
            for j in xrange(k):
                buckets[j] += nums[i]
                if buckets[j] <= target and walk(i+1):
                    return True
                buckets[j] -= nums[i]
                if buckets[j] == 0: # we always start from first bucket, so no need to try following empty buckets
                    break
            return False        
        
        return walk(0)
