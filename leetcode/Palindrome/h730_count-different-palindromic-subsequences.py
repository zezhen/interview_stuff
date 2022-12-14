'''
https://leetcode.com/problems/count-different-palindromic-subsequences/description/

Given a string S, find the number of different non-empty palindromic subsequences in S, and return that number modulo 10^9 + 7.

A subsequence of a string S is obtained by deleting 0 or more characters from S.

A sequence is palindromic if it is equal to the sequence reversed.

Two sequences A_1, A_2, ... and B_1, B_2, ... are different if there is some i for which A_i != B_i.

Example 1:
Input: 
S = 'bccb'
Output: 6
Explanation: 
The 6 different non-empty palindromic subsequences are 'b', 'c', 'bb', 'cc', 'bcb', 'bccb'.
Note that 'bcb' is counted only once, even though it occurs twice.
Example 2:
Input: 
S = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
Output: 104860361
Explanation: 
There are 3104860382 different non-empty palindromic subsequences, which is 104860361 modulo 10^9 + 7.
Note:

The length of S will be in the range [1, 1000].
Each character S[i] will be in the set {'a', 'b', 'c', 'd'}.
'''

class Solution(object):
    def countPalindromicSubsequences(self, S):
        """
        :type S: str
        :rtype: int
        """

# refer to Java solution below, from https://leetcode.com/problems/count-different-palindromic-subsequences/discuss/109509
'''
class Solution {
    int div=1000000007;
    public int countPalindromicSubsequences(String S) {    
        TreeSet[] characters = new TreeSet[26];
        int len = S.length();
        
        for (int i = 0; i < 26; i++) characters[i] = new TreeSet<Integer>();
        
        for (int i = 0; i < len; ++i) {
            int c = S.charAt(i) - 'a';
            characters[c].add(i);
        }
        Integer[][] dp = new Integer[len+1][len+1];
        return memo(S,characters,dp, 0, len);
    }
    
    public int memo(String S,TreeSet<Integer>[] characters,Integer[][] dp,int start,int end){
        if (start >= end) return 0;
        if(dp[start][end]!=null) return dp[start][end];
       
            long ans = 0;
            for(int i = 0; i < 26; i++) {
                // for python, binary search can make it
                Integer new_start = characters[i].ceiling(start);
                Integer new_end = characters[i].lower(end);
                if (new_start == null || new_start >= end) continue;
                // for case 'a..' or '..a'
                ans++;
                // for case 'a...a'
                if (new_start != new_end) ans++;
                // go to internal
                ans+= memo(S,characters,dp,new_start+1,new_end);
                
            }
            dp[start][end] = (int)(ans%div);
            return dp[start][end];
    }
    
}
'''