'''
https://leetcode.com/problems/student-attendance-record-i
https://leetcode.com/articles/student-attendance-record-i
You are given a string representing an attendance record for a student. The record only contains the following three characters:



'A' : Absent. 
'L' : Late.
 'P' : Present. 




A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).    

You need to return whether the student could be rewarded according to his attendance record.

Example 1:

Input: "PPALLP"
Output: True



Example 2:

Input: "PPALLL"
Output: False




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
            
s = Solution()
print s.checkRecord(1) == 3
print s.checkRecord(2) == 8
print s.checkRecord(3) == 19
print s.checkRecord(10) == 3536
print s.checkRecord(100)