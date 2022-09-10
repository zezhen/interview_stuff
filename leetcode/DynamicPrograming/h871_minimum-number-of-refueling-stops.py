'''
https://leetcode.com/problems/minimum-number-of-refueling-stops/description/

A car travels from a starting position to a destination which is target miles east of the starting position.

Along the way, there are gas stations.  Each station[i] represents a gas station that is station[i][0] miles east of the starting position, and has station[i][1] liters of gas.

The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it.  It uses 1 liter of gas per 1 mile that it drives.

When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.

What is the least number of refueling stops the car must make in order to reach its destination?  If it cannot reach the destination, return -1.

Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there.  If the car reaches the destination with 0 fuel left, it is still considered to have arrived.

 

Example 1:

Input: target = 1, startFuel = 1, stations = []
Output: 0
Explanation: We can reach the target without refueling.
Example 2:

Input: target = 100, startFuel = 1, stations = [[10,100]]
Output: -1
Explanation: We can't reach the target (or even the first gas station).
Example 3:

Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
Output: 2
Explanation: 
We start with 10 liters of fuel.
We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
We made 2 refueling stops along the way, so we return 2.
 

Note:

1 <= target, startFuel, stations[i][1] <= 10^9
0 <= stations.length <= 500
0 < stations[0][0] < stations[1][0] < ... < stations[stations.length-1][0] < target
'''

class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """

        # dp[i][j] means the max reachable position when ith fuel at station j
        # dp[i][j] = max(dp[i-1][k]+stations[k][1]), if dp[i-1][k] >= station[j][0]
        # min i that dp[i][*] >= target
        if startFuel >= target: return 0
        if not stations and startFuel < target or startFuel < stations[0][0]: return -1

        n = len(stations)
        dp = [[0] * n for _ in xrange(n)]

        for j in xrange(n):
            if startFuel >= stations[j][0]:
                dp[0][j] = startFuel + stations[j][1]
                if dp[0][j] >= target: return 1

        for i in xrange(1, n+1):
            for j in xrange(i, n):
                for k in xrange(j):
                    # print i, j, k, dp[i-1][k], stations[j][0]
                    if dp[i-1][k] >= stations[j][0]:
                        dp[i][j] = max(dp[i][j], dp[i-1][k] + stations[j][1])
                        if dp[i][j] >= target: return i+1

        return -1

    def minRefuelStops_fastest(self, target, cur, s):
        pq = []
        res = i = 0
        while cur < target:
            while i < len(s) and s[i][0] <= cur:
                heapq.heappush(pq, -s[i][1])
                i += 1
            if not pq: return -1
            cur += -heapq.heappop(pq)
            res += 1
        return res


s = Solution()
print s.minRefuelStops(100, 25, [[25,25],[50,25],[75,25]])  == 3
print s.minRefuelStops(1, 0, [[1,1]])  == -1
print s.minRefuelStops(1, 1, []) == 0
print s.minRefuelStops(2, 1, []) == -1
print s.minRefuelStops(3, 1, [[1,1]]) == -1
print s.minRefuelStops(100, 1, [[10,100]]) == -1
print s.minRefuelStops(100, 10, [[10,60],[20,30],[30,30],[60,40]]) == 2

print s.minRefuelStops(1000000,53667,[[6950,13028],[21145,25000],[38690,6304],[54352,42300],[56808,45976],[63983,37886],[68419,15751],[69504,8075],[85043,32434],[92914,50646],[109806,43101],[112920,7430],[116008,35223],[121846,46938],[128528,48626],[128560,49460],[135306,1996],[151134,26992],[157586,52788],[166585,44818],[167892,13581],[202994,11028],[217878,18871],[241339,51351],[248208,38733],[257762,32253],[277792,36820],[288531,19642],[331194,18080],[348898,35356],[349346,4671],[359199,17610],[360009,5527],[368757,14195],[396664,14932],[401524,49201],[402539,35084],[422674,5352],[427795,14717],[431106,42724],[431917,46730],[437958,45353],[458031,9710],[467378,39191],[488467,49031],[495827,34298],[501568,35856],[504829,5089],[511736,30952],[516011,8269],[516355,51173],[519876,32562],[528434,18530],[561784,13822],[565838,38935],[574928,24104],[582225,5169],[593508,27144],[603060,31587],[613347,46986],[621815,47051],[641640,3362],[654360,37738],[676653,41273],[686787,13056],[695695,21872],[700010,25196],[721310,32491],[724872,26252],[725214,42539],[750190,15189],[765068,3418],[766642,23799],[769842,20742],[770378,44127],[777325,16075],[783687,15299],[783886,44121],[820968,6557],[822189,1196],[822795,49842],[824231,52596],[848150,39409],[854444,25292],[878221,22784],[889948,21445],[893844,17898],[895155,33036],[904112,40321],[911401,49930],[913887,9344],[929823,38731],[939245,45498],[952152,45798],[958422,53539],[979783,10569],[985338,5294],[991430,21666],[991970,35896],[996672,36853]]) == 20





