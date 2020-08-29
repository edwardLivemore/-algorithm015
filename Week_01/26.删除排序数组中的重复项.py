#
# @lc app=leetcode.cn id=26 lang=python
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lens = len(nums)
        if lens == 0:
            return 0
        i,j = 0,1
        for j in range(lens):
            if nums[j] != nums[i]:
                i = i + 1
                nums[i] = nums[j]
        return i + 1
                
# @lc code=end

