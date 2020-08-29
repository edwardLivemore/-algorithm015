#
# @lc app=leetcode.cn id=189 lang=python
#
# [189] 旋转数组
#

# @lc code=start
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        lens = len(nums)
        if lens == k or lens <= 1:
            return
        k, count, start, current, prev = k % lens, 0, 0, 0, 0
        while count < lens:
            prev = nums[start]
            current = start
            while True:
                next = (current + k) % lens
                temp = nums[next]
                nums[next] = prev
                prev = temp
                current = next
                count += 1
                if start == current:
                    break
            start += 1
# @lc code=end
