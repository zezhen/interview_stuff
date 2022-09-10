'''
https://leetcode.com/problems/my-calendar-ii
https://leetcode.com/articles/my-calendar-ii

Implement a MyCalendarTwo class to store your events. A new event can be added if adding the event will not cause a triple booking.

Your class will have one method, book(int start, int end).  Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.

A triple booking happens when three events have some non-empty intersection (ie., there is some time that is common to all 3 events.)

For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a triple booking.  Otherwise, return false and do not add the event to the calendar.


Your class will be called like this:
MyCalendar cal = new MyCalendar();
MyCalendar.book(start, end)

Example 1:

MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(50, 60); // returns true
MyCalendar.book(10, 40); // returns true
MyCalendar.book(5, 15); // returns false
MyCalendar.book(5, 10); // returns true
MyCalendar.book(25, 55); // returns true
Explanation: 
The first two events can be booked.  The third event can be double booked.
The fourth event (5, 15) can't be booked, because it would result in a triple booking.
The fifth event (5, 10) can be booked, as it does not use time 10 which is already double booked.
The sixth event (25, 55) can be booked, as the time in [25, 40) will be double booked with the third event;
the time [40, 50) will be single booked, and the time [50, 55) will be double booked with the second event.



Note:
The number of calls to MyCalendar.book per test case will be at most 1000.
In calls to MyCalendar.book(start, end), start and end are integers in the range [0, 10^9].
'''

import bisect

class MyCalendarTwo(object):
        
    def __init__(self):
        self.room = {'start':[],'end':[]}
        self.overlap = {'start':[],'end':[]}
    
    def check_overlap(self, space, start, end):
        stime, etime = space['start'], space['end']
        index = bisect.bisect_left(stime, start)
        
        overlap = []
        for offset in range(-1, 2):
            if 0 <= index + offset < len(stime):
                is_overlap = self._overlap(start, end, stime[index + offset], etime[index + offset])
                if is_overlap:
                    overlap.append((max(start, stime[index + offset]), min(end, etime[index + offset])))
        return index, overlap
    
    def insert(self, room, index, start, end):
        if index >= len(room['start']):
            room['start'].append(start)
            room['end'].append(end)
        else:
            room['start'].insert(index, start)
            room['end'].insert(index, end)
    
    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """

        index, overlap = self.check_overlap(self.room, start, end)
        if len(overlap) == 0:
            self.insert(self.room, index, start, end)
        else:
            tmp_cache = []
            for (ols, ole) in overlap:
                i, ov = self.check_overlap(self.overlap, ols, ole)
                if len(ov) > 0: return False
                tmp_cache.append((i, ols, ole))
            
            self.insert(self.room, index, start, end)
            for i, ols, ole in reversed(tmp_cache):
                self.insert(self.overlap, i, ols, ole)

        return True
    
    def _overlap(self, s1, e1, s2, e2):
        return max(s1, s2) < min(e1, e2)

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)