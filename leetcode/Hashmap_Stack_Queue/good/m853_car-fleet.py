'''
https://leetcode.com/problems/car-fleet
https://leetcode.com/articles/car-fleet
N cars are going to the same destination along a one lane road.  The destination is target miles away.

Each car i has a constant speed speed[i] (in miles per hour), and initial position position[i] miles towards the target along the road.

A car can never pass another car ahead of it, but it can catch up to it, and drive bumper to bumper at the same speed.

The distance between these two cars is ignored - they are assumed to have the same position.

A car fleet is some non-empty set of cars driving at the same position and same speed.  Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.


How many car fleets will arrive at the destination?

 

Example 1:


Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
The cars starting at 10 and 8 become a fleet, meeting each other at 12.
The car starting at 0 doesn't catch up to any other car, so it is a fleet by itself.
The cars starting at 5 and 3 become a fleet, meeting each other at 6.
Note that no other cars meet these fleets before the destination, so the answer is 3.



Note:


	0 <= N <= 10 ^ 4
	0 < target <= 10 ^ 6
	0 < speed[i] <= 10 ^ 6
	0 <= position[i] < target
	All initial positions are different.

'''
class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        if not position or not speed: return 0
        
        cars = zip(position, speed)
        cars.sort()

        fleets = 1
        # start from tail, if there is bottleneck ahead, 
        # all cars afterward will bump into one fleet
        for i in xrange(len(cars)-1, 0, -1):
            # i-1 cannot catch up with lower/equal speed and less position.
            if cars[i][1] >= cars[i-1][1]:
                fleets += 1
            else:
                bump_time = (cars[i][0] - cars[i-1][0]) * 1.0 / (cars[i-1][1] - cars[i][1])
                bump_pos = cars[i][0] + bump_time * cars[i][1]
                if bump_pos > target: # cannot catch up before reach target
                    fleets += 1
                else:
                    # i-1 and i become one fleet, whose parameters are same as car[i]
                    cars[i-1] = cars[i] # update i-1

        return fleets

s = Solution()
print s.carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]) == 3
print s.carFleet(target = 10, position = [6,8], speed = [3,2]) == 2
print s.carFleet(target = 10, position = [0,4,2], speed = [2,1,3]) == 1
