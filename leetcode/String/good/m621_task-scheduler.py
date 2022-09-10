'''
https://leetcode.com/problems/task-scheduler/description/

Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks.Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

 

Example:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
 

Note:

The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].
'''

# we don't need actually arrange them. Instead we only need to get the total idles we need and the answer to problem is just number of idles + number of tasks.
# https://leetcode.com/problems/task-scheduler/discuss/104500
'''
public class Solution {
    public int leastInterval(char[] tasks, int n) {
        int[] counter = new int[26];
        int max = 0;
        int maxCount = 0;
        for(char task : tasks) {
            counter[task - 'A']++;
            if(max == counter[task - 'A']) {
                maxCount++;
            }
            else if(max < counter[task - 'A']) {
                max = counter[task - 'A'];
                maxCount = 1;
            }
        }
        
        int partCount = max - 1;
        int partLength = n - (maxCount - 1);
        int emptySlots = partCount * partLength;
        int availableTasks = tasks.length - max * maxCount;
        int idles = Math.max(0, emptySlots - availableTasks);
        
        return tasks.length + idles;
    }
}
'''

return Math.max(tasks.length, (c[25] - 1) * (n + 1) + 25 - i);

class Solution(object):

    def leastInterval(self, tasks, n):
        c = collections.Counter(tasks)
        mc, tie_ct = c.most_common(1)[0][1], 0
        for k, v in c.most_common()[1:]:
            if v == mc:
                tie_ct += 1
            else:
                break
        
        return max(len(tasks), (mc-1)*n + mc + tie_ct)

        # (mc-1)*n - number of gaps between the most common characters
        # mc - frequency of the most common character
        # tie_ct - number of characters having the same frequency as the most common character (excluding the most common character)

    def leastInterval_too_much(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # count tasks, the more one task, the higher priority we should place it
        task_count = {}
        for task in tasks:
            if task not in task_count:
            	# [last_position, residual], negative residual to make ascending order
                task_count[task] = [-1, -1, task]
            else:    
                task_count[task][1] -= 1

        tasks = self.update_order(task_count.values(), 0, n)

        pos = 0
        tmp = []
        while len(tasks) > 0:
        	# print tmp, tasks
        	last_pos, residual, _ = tasks[0]
        	if last_pos < 0 or pos - last_pos > n:
        		tasks[0][0] = pos
        		# negative residual add one means positive one minutes one
        		tasks[0][1] += 1
        		if tasks[0][1] == 0: tasks.pop(0)
        		# tmp.append(taskname)
        		self.update_order(tasks, pos, n)
        	else:
        		# add idel
        		# tmp.append('idel')
        		pass
        	pos += 1

        # print tmp
        return pos

    # order the tasks, we need to consider two factors
    # 1. last position. 
    #    if one task is in n size window, lower its priority, 
    #    if it's outside of the window, set same priority as others (we set -1 here)
    # 2. residual count. The more amount, the higher priority
    def update_order(self, tasks, pos, n):
    	tasks.sort(key=lambda t: (t[0] if pos - t[0] < n else -1, t[1]))
    	return tasks