#
# @lc app=leetcode.cn id=45 lang=python
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lens = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(lens - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
                    if end >= lens - 1:
                        break
        return step
# print(Solution().jump([2,3,1,2,4,2,3]))
# @lc code=end

