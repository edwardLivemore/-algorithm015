#
# @lc app=leetcode.cn id=300 lang=python
#
# [300] 最长上升子序列
#

# @lc code=start
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        lens = len(nums)
        dp = []
        for i in range(lens):
            dp.append(1)
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

# @lc code=end

