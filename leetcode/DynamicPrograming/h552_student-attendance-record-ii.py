'''
https://leetcode.com/problems/student-attendance-record-ii
https://leetcode.com/articles/student-attendance-record-ii
Given a positive integer n, return the number of all possible attendance records with length n, which will be regarded as rewardable. The answer may be very large, return it after mod 109 + 7.

A student attendance record is a string that only contains the following three characters:



'A' : Absent. 
'L' : Late.
 'P' : Present. 




A record is regarded as rewardable if it doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

Example 1:

Input: n = 2
Output: 8 
Explanation:
There are 8 records with length 2 will be regarded as rewardable:
"PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" won't be regarded as rewardable owing to more than one absent times. 



Note:
The value of n won't exceed 100,000.



'''
class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        mod = 10**9 + 7
        absent_one_late, absent_present, absent_two_late = 0,0,0
        no_absent_one_late, no_absent_present, no_absent_two_late = 0,0,0

        # first one
        absent_present = no_absent_present = no_absent_one_late = 1
        for i in xrange(1, n):
            # add absent
            ap = no_absent_one_late + no_absent_present + no_absent_two_late

            # add one late
            aol = absent_present
            naol = no_absent_present

            atl = absent_one_late
            natl = no_absent_one_late

            # add present
            ap += absent_one_late + absent_present + absent_two_late
            nap = no_absent_one_late + no_absent_present + no_absent_two_late
            
            absent_one_late, absent_present, absent_two_late = aol % mod, ap % mod, atl % mod
            no_absent_one_late, no_absent_present, no_absent_two_late = naol % mod, nap % mod, natl % mod
        
        # print absent_one_late, absent_present, absent_two_late, no_absent_one_late, no_absent_present, no_absent_two_late
        return sum([absent_one_late, absent_present, absent_two_late, no_absent_one_late, no_absent_present, no_absent_two_late]) % mod