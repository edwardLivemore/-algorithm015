#
# @lc app=leetcode.cn id=33 lang=python
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 二分查找
        result = -1
        if nums:
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] == target:
                    return mid
                if nums[low] <= nums[mid]:
                    # 左侧升序
                    if nums[low] <= target < nums[mid]:
                        # 左侧查找
                        high = mid - 1
                    else:
                        low = mid + 1
                else:
                    # 右侧升序
                    if nums[mid] < target <= nums[high]:
                        # 右侧查找
                        low = mid + 1
                    else:
                        high = mid - 1
        return result
# print(Solution().search([4,5,6,7,0,1,2], 0))
# print(Solution().search([3,1], 1))
# @lc code=end

