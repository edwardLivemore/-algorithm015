#
# @lc app=leetcode.cn id=860 lang=python
#
# [860] 柠檬水找零
#

# @lc code=start
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five_left, ten_left = 0, 0
        for i in bills:
            if i == 5:
                five_left += 1
            elif i == 10:
                if not five_left:
                    return False
                five_left -= 1
                ten_left += 1
            else:
                if ten_left and five_left:
                    ten_left -= 1
                    five_left -= 1
                elif five_left >= 3:
                    five_left -= 3
                else:
                    return False
        return True
# @lc code=end

