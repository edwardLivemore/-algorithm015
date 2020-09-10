#
# @lc app=leetcode.cn id=47 lang=python
#
# [47] 全排列 II
#

# @lc code=start
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 回溯 + 剪枝
        result = []
        used = [False for i in range(len(nums))]
        
        def dfs(nums, size, path):
            if len(path) == size:
                result.append(path)
                return

            for i in range(size):
                if not used[i]:
                    if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                        continue
                    used[i] = True
                    dfs(nums, size, path + [nums[i]])
                    used[i] = False

        if nums:
            nums.sort()
            dfs(nums, len(nums), [])

        return result
# @lc code=end

