#
# @lc app=leetcode.cn id=283 lang=python
#
# [283] 移动零
#

# @lc code=start
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return 0

        i = 0
        for j in range(len(nums)):
            if nums[j]:
                nums[i], nums[j]  = nums[j], nums[i]
                i += 1
# @lc code=end

