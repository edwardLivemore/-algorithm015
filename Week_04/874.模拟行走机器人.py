#
# @lc app=leetcode.cn id=874 lang=python
#
# [874] 模拟行走机器人
#

# @lc code=start
class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        result = 0
        obstaclesSet = set(map(tuple, obstacles))

        if commands:
            dic_index, x, y = 0, 0, 0
            for cmd in commands:
                if cmd == -1:
                    # turn right
                    dic_index = (dic_index + 1) % 4
                elif cmd == -2:
                    # turn left
                    dic_index = (dic_index - 1) % 4
                else:
                    for step in range(cmd):
                        # 判断是否有障碍物
                        if (x + dx[dic_index], y + dy[dic_index]) not in obstaclesSet:
                            # 无障碍物
                            x, y = x + dx[dic_index], y + dy[dic_index]
                            result = max(result, x * x + y * y)
        return result

# print(Solution().robotSim([4,-1,4,-2,4], [[2,4], [1,4]]))
# @lc code=end
