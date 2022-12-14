'''
https://leetcode.com/problems/number-of-music-playlists
https://leetcode.com/articles/number-of-music-playlists
Your music player contains N different songs and she wants to listen to L (not necessarily different) songs during your trip.  You create a playlist so that:


	Every song is played at least once
	A song can only be played again only if K other songs have been played


Return the number of possible playlists.  As the answer can be very large, return it modulo 10^9 + 7.

 




Example 1:


Input: N = 3, L = 3, K = 1
Output: 6
Explanation: There are 6 possible playlists. [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1].



Example 2:


Input: N = 2, L = 3, K = 0
Output: 6
Explanation: There are 6 possible playlists. [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2, 1], [2, 1, 2], [1, 2, 2]



Example 3:


Input: N = 2, L = 3, K = 1
Output: 2
Explanation: There are 2 possible playlists. [1, 2, 1], [2, 1, 2]




 

Note:


	0 <= K < N <= L <= 100

'''

class Solution(object):
    def numMusicPlaylists(self, N, L, K):
        """
        :type N: int
        :type L: int
        :type K: int
        :rtype: int
        """

        '''
        dp[i][j] denotes the solution of i songs with j different songs. So the final answer should be dp[L][N]

        Think one step before the last one, there are only cases for the answer of dp[i][j]
        case 1 (the last added one is new song): listen i - 1 songs with j - 1 different songs, then the last one is definitely new song with the choices of N - (j - 1).
        Case 2 (the last added one is old song): listen i - 1 songs with j different songs, then the last one is definitely old song with the choices of j
        if without the constraint of K, the status equation will be
        dp[i][j] = dp[i-1][j-1] * (N - (j-1)) + dp[i-1][j] * j

        If with the constaint of K, there are also two cases
        Case 1: no changes since the last added one is new song. Hence, there is no conflict
        Case 2: now we don't have choices of j for the last added old song. It should be updated j - k because k songs can't be chosed from j - 1 to j - k. However, if j <= K, this case will be 0 because only after choosing K different other songs, old song can be chosen.

        if (j > k)
        dp[i][j] = dp[i-1][j-1] * (N- (j-1)) + dp[i-1][j] * (j-k)
        else
        dp[i][j] = dp[i-1][j-1] * (N- (j-1))

        the code below is rotate i and j

        '''
        dp = [[0 for i in range(L + 1)] for j in range(N + 1)]
        for i in range(K + 1, N + 1):
            for j in range(i, L + 1):
                if i == j or i == K + 1:
                    dp[i][j] = math.factorial(i)
                else:
                    dp[i][j] = dp[i - 1][j - 1] * i + dp[i][j - 1] * (i - K)
        return dp[N][L] % (10**9 + 7)

s  = Solution()
print s.numMusicPlaylists(3, 3, 1)
print s.numMusicPlaylists(2, 3, 0)




