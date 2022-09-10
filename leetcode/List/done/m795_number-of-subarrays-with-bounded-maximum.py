'''
https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum
https://leetcode.com/articles/number-of-subarrays-with-bounded-maximum
We are given an array A of positive integers, and two positive integers L and R (L <= R).

Return the number of (contiguous, non-empty) subarrays such that the value of the maximum array element in that subarray is at least L and at most R.


Example :
Input: 
A = [2, 1, 4, 3]
L = 2
R = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].


Note:


	L, R  and A[i] will be an integer in the range [0, 10^9].
	The length of A will be in the range of [1, 50000].

'''
import collections
class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        
        counter = collections.defaultdict(int)

        left = ans = 0
        inRange = 0

        for right, a in enumerate(A, 1):
            if A <= a <= R:
                inRange += 1
                counter[a] += 1

            if a > R:


'''
class Solution {
public int numSubarrayBoundedMax(int[] A, int L, int R) {
    int j=0,count=0,res=0;
    
    for(int i=0;i<A.length;i++){
        if(A[i]>=L && A[i]<=R){
            res+=i-j+1;count=i-j+1;
        }
        else if(A[i]<L){
            res+=count;
        }
        else{
            j=i+1;
            count=0;
        }
    }
    return res;
}
}
'''