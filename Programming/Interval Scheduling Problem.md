# Interval Scheduling Problem
----

**Interval scheduling** is a class of problems in computer science, particularly in the area of algorithm design. The problems consider a set of tasks. Each task is represented by an interval describing the time in which it needs to be executed. For instance, task A might run from 2:00 to 5:00, task B might run from 4:00 to 10:00 and task C might run from 9:00 to 11:00. A subset of intervals is compatible if no two intervals overlap. For example, the subset {A,C} is compatible, as is the subset {B}; but neither {A,B} nor {B,C} are compatible subsets, because the corresponding intervals within each subset overlap.


1.  The **interval scheduling maximization problem** (ISMP) is to find a largest compatible set - a set of non-overlapping intervals of maximum size. The goal here is to execute as many tasks as possible.



> The following greedy algorithm does find the **optimal** solution:

1.  Select the interval, x, with the earliest finishing time.
2.  Remove x, and all intervals intersecting x, from the set of candidate intervals.
3.  Repeat until the set of candidate intervals is empty.

         A more formal explanation is given by a [Charging argument](https://en.wikipedia.org/wiki/Charging_argument).



*   [meeting-rooms](https://leetcode.com/problems/meeting-rooms): 给定Interval (start, end), 检查一个room能否容纳所有meetings. 
    *   按start排序, 检查end与下一个start是否重叠即可.
*   [meeting-rooms-ii](https://leetcode.com/problems/meeting-rooms-ii): 给定Intervals, 至少需要多少个room才能容纳所有meetings. ISMP的变形, 排序starts和ends, 从最小的end开始, 检查冲突, 有冲突就需要多一个room
    *   starts = sorted(map(lambda t:t\[0\], intervals))
    *   ends = sorted(map(lambda t:t\[1\], intervals))
    *   rooms, endIndex = 0,0
    *   for s in starts:
    *       if s < ends\[endIndex\]:
    *           rooms += 1
    *       else:
    *           endIndex += 1
    *   return rooms
*   [non-overlapping-intervals](https://leetcode.com/problems/non-overlapping-intervals): 删除最少的Interval使得不重叠. 反过来就是ISMP问题
    *   end = float('-inf')
    *   count = 0
    *   for s,e in sorted(intervals, key=lambda i: i.end):
    *       if s >= end:
    *           end = e
    *           count += 1
    *   return len(intervals) - count
*   [my-calendar-i](https://leetcode.com/problems/my-calendar-i)
    *   class MyCalendar:
    *       def \_\_init\_\_(self):
    *           self.calendar = \[\]
    *   
    *       def book(self, start, end):
    *           for i, j in self.calendar:        # O(n^2) time complexity, need binary search tree for O(nlogn)
    *               if start < j and end > i:    # check overlap
    *                   return False
    *           self.calendar.append((start, end))
    *           return True
*   [my-calendar-ii](https://leetcode.com/problems/my-calendar-ii)
    *   class MyCalendarTwo:
    *       def \_\_init\_\_(self):
    *           self.overlaps = \[\]   # can only overlap once   
    *           self.calendar = \[\]
    *   
    *       def book(self, start, end):
    *           for i, j in self.overlaps:
    *               if start < j and end > i:
    *                   return False
    *           for i, j in self.calendar:
    *               if start < j and end > i:
    *                   self.overlaps.append((max(start, i), min(end, j)))
    *           self.calendar.append((start, end))
    *           return True
*   [my-calendar-iii](https://leetcode.com/problems/my-calendar-iii)
    *   credit to [@alexander](https://leetcode.com/alexander/), this solution works for meeting-root and calendar problems. refer to [https://leetcode.com/problems/meeting-rooms-ii/discuss/203658](https://leetcode.com/problems/meeting-rooms-ii/discuss/203658/HashMapTreeMap-resolves-Scheduling-Problem)
    *   \`This is to find the maximum number of concurrent ongoing event at any time.\`
    *   We can log the start & end of each event on the timeline, each start add a new ongoing event at that time, each end terminate an ongoing event. Then we can scan the timeline to figure out the maximum number of ongoing event at any time.
    *   The most intuitive data structure for timeline would be array, but the time spot we have could be very sparse, so we can use sorted map to simulate the time line to save space.
    *   
    *   import collections
    *   class MyCalendarThree(object):
    *       def \_\_init\_\_(self):
    *           self.timeline = collections.defaultdict(int)
    *   
    *       def book(self, start, end):
    *           self.timeline\[start\] += 1
    *           self.timeline\[end\] -= 1
    *           ongoing, k = 0, 0
    *           for t in sorted(self.timeline.keys()):
    *               ongoing += self.timeline\[t\]
    *               k = max(k, ongoing)
    *           return k
*   [merge-intervals](https://leetcode.com/problems/merge-intervals): 给定多个Interval, 合并重叠的intervals, 跟meeting-room类似
    *   def merge(self, intervals):
    *       if not intervals: return \[\]
    *       intervals.sort(key=lambda t: t.start)
    *       ans = \[intervals\[0\]\]
    *       for interval in intervals\[1:\]:
    *           s, e = interval.start, interval.end
    *           lastOne = ans\[-1\]
    *           if s > lastOne.end:
    *               ans.append(Interval(s, e))
    *           else:
    *               lastOne.end = max(e, lastOne.end)
    *       return ans
*   [insert-interval](https://leetcode.com/problems/insert-interval/description/) (hard): Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary)
    *   check intervals one by one, if overlap, then merge, add into a new list
*   [find-right-interval](https://leetcode.com/problems/find-right-interval/description/)
    *   def findRightInterval(self, intervals):
    *    l = sorted((e.start, i) for i, e in enumerate(intervals))
    *    res = \[\]
    *    for e in intervals:
    *           **r = bisect.bisect\_left(l, (e.end,))**          # this is awesome
    *    res.append(l\[r\]\[1\] if r < len(l) else \-1)
    *       return res


**Reference**
\[1\] [https://en.wikipedia.org/wiki/Interval\_scheduling](https://en.wikipedia.org/wiki/Interval_scheduling)

----

- Date: 2018-12-23
- Tags: #Interview/Programing 



