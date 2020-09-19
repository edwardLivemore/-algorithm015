#
# @lc app=leetcode.cn id=55 lang=python
#
# [55] 跳跃游戏
#

# @lc code=start 
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums:
            lens = len(nums)
            endreachable = lens - 1
            for i in range(lens - 1, -1, -1):
                if nums[i] + i >= endreachable:
                    endreachable = i
            return endreachable == 0
        return False
# @lc code=end

