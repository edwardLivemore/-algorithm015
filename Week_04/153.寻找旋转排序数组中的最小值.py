#
# @lc app=leetcode.cn id=153 lang=python
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2
            if low == mid:
                if nums[low] > nums[high]:
                    return nums[high]
                else:
                    return nums[low]

            if nums[low] > nums[mid]:
                high = mid
            else:
                if nums[mid] < nums[high]:
                    high = mid
                else:
                    low = mid

# print(Solution().findMin([1,2,3]))
# @lc code=end

