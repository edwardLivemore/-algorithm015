#
# @lc app=leetcode.cn id=46 lang=python
#
# [46] 全排列
#

# @lc code=start
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        def helper(sublist, n, nums):
            if len(sublist) == n:
                result.append(sublist)            
                return

            for i in nums:
                new_nums = nums[:]
                new_nums.remove(i)
                helper(sublist + [i], n, new_nums)
        
        helper([], len(nums), nums)
        return result
# @lc code=end

