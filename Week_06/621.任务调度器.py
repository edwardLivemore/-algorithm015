#
# @lc app=leetcode.cn id=621 lang=python
#
# [621] 任务调度器
#

# @lc code=start
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        map = [0] * 26
        for task in tasks:
            map[ord(task) - ord('A')] += 1
        map.sort()
        max_val = map[25] - 1
        idle_slots = max_val * n
        i = 24
        while i >= 0 and map[i] > 0:
            idle_slots -= min(max_val, map[i])
            i -= 1
        return (idle_slots + len(tasks)) if idle_slots > 0 else len(tasks) 

# print(Solution().leastInterval(["A","A","A","B","B","B"], 2))        
# @lc code=end

