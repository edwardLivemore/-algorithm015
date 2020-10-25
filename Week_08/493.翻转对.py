#
# @lc app=leetcode.cn id=493 lang=python
#
# [493] 翻转对
#

# @lc code=start
class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        return self.mergeSort(nums, 0, len(nums) - 1)

    def mergeSort(self, nums, left, right):
        if left >= right:
            return 0
        
        mid = left + ((right - left) >> 1)
        count = self.mergeSort(nums, left, mid) + self.mergeSort(nums, mid + 1, right)
        cache = []
        i, t = left, left
        for j in range(mid + 1, right + 1):
            while i <= mid and nums[i] <= 2 * nums[j]:
                i += 1
            while t <= mid and nums[t] < nums[j]:
                cache.append(nums[t])
                t += 1
            cache.append(nums[j])
            count += mid - i + 1
        while t <= mid:
            cache.append(nums[t])
            t += 1
        nums[left : right + 1] = cache
        return count
# @lc code=end

