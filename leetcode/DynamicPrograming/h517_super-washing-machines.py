'''
https://leetcode.com/problems/super-washing-machines
You have n super washing machines on a line. Initially, each washing machine has some dresses or is empty. 


For each move, you could choose any m (1 <= m <= n) washing machines, and pass one dress of each washing machine to one of its adjacent washing machines  at the same time .  

Given an integer array representing the number of dresses in each washing machine from left to right on the line, you should find the minimum number of moves to make all the washing machines have the same number of dresses. If it is not possible to do it, return -1.

Example1

Input: [1,0,5]

Output: 3

Explanation: 
1st move:    1     0 <-- 5    =>    1     1     4
2nd move:    1 <-- 1 <-- 4    =>    2     1     3    
3rd move:    2     1 <-- 3    =>    2     2     2   


Example2

Input: [0,3,0]

Output: 2

Explanation: 
1st move:    0 <-- 3     0    =>    1     2     0    
2nd move:    1     2 --> 0    =>    1     1     1     


Example3

Input: [0,2,0]

Output: -1

Explanation: 
It's impossible to make all the three washing machines have the same number of dresses. 




Note:

The range of n is [1, 10000].
The range of dresses number in a super washing machine is [0, 1e5].

'''
class Solution(object):
    # don't undertand the wording correctly after read the example 
    # 1st move: 2 --> 0 0 <-- 2 => 1 1 1 1
    # we can select multiple adjacent washing machines and pass one dress to each
    # but each time, each machine can only give-out one dress
    # while each machine can receive-in at most two dress

    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """

        if sum(machines) % len(machines) != 0: return -1

        average = sum(machines) / len(machines)
        ans = count = 0
        for load in machines:
            count += load - average
            ans = max(max(ans, abs(count)), load - average)
        return ans

        '''
        credit to https://leetcode.com/problems/super-washing-machines/discuss/99185
        explanation:
        we have machines [0,0,11,5], total is 16, average is 4, convert gain/lose array and get [-4,-4,7,1]
        transfer the array to [0,0,0,0] can through [-4,-4,7,1] -> [0,-8,7,1] -> [0,0,-1,1] -> [0,0,0,0]
        max move is 8
        
        1. The logic here is to find the max/peak 'throughput' going from the leftmost washer to the rightmost washer, and the max of the 'GIVE-OUT' washer. The max of these two is the answer. (1) We want the max/peak of the 'throughput' because for washer(s) from one side, giving/receiving its load to/from washer(s) from the other side, their to-give/to-receive loads accumulate during the transportation, like for [-2 -2 0 1, 3]. (its original nums could be [1, 1, 3, 4, 6]), the leftmost -2 cannot be balanced directly without going through the 2nd -2. So it is the same as [0, -4, 0, 1, 3] or [0, 0, -4, 1, 3]. Only adjacent machines can transfer loads, and potentially balance each other or accumulate to-balance values. Here, 4 is the max absolute to-balance value we found going from left to right, so it is 4.
        2. Why us load-avg? Because [-1, 2 ,-1] and [1, -2, 1] are different!! The former can be balanced with 2 steps, but the latter can be balanced with only 1 step! That is to say, giving out loads and receiving loads are different. One machines can at most give 1 load each step, but can receive at most 2 loads each step. Therefore, finding the max positive to-balance load is what we want. Like [0, -7, 8, -1], no matter what you do or how you do it, the machines with 8 loads need no less than 8 to balance itself and become 0.
        '''

    def findMinMoves_dp(self, machines):
        '''
        credit to https://leetcode.com/problems/super-washing-machines/discuss/99181
        For a single machine, necessary operations is to transfer dresses from one side to another until sum of both sides and itself reaches the average number. We can calculate (required dresses) - (contained dresses) of each side as L and R:

        L > 0 && R > 0: both sides lacks dresses, and we can only export one dress from current machines at a time, so result is abs(L) + abs(R)
        L < 0 && R < 0: both sides contains too many dresses, and we can import dresses from both sides at the same time, so result is max(abs(L), abs(R))
        L < 0 && R > 0 or L >0 && R < 0: the side with a larger absolute value will import/export its extra dresses from/to current machine or other side, so result is max(abs(L), abs(R))
        '''
        n = len(machines)
        acc = [0] * (n + 1)
        for i in xrange(n):
            acc[i+1] = acc[i] + machines[i]

        if acc[n] % n != 0: return -1
        average = acc[n] / n
        ans = 0
        for i in xrange(n):
            l = average * i - acc[i]
            r = average * (n - 1 - i)  - (acc[n] - acc[i] - machines[i])

            if l > 0 and r > 0:
                ans = max(ans, abs(l) + abs(r))
            else:
                ans = max(ans, abs(l), abs(r))
        return ans


s = Solution()
print s.findMinMoves([1,0,5]) == 3
print s.findMinMoves([0,3,0]) == 2
print s.findMinMoves([0,2,0]) == -1
print s.findMinMoves([1,1,1,2,0]) == 1
print s.findMinMoves([0,0,0]) == 0
print s.findMinMoves([4,0,0,4]) == 2



